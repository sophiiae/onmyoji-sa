import random
from typing import Optional, List
import copy
import operator
import inflection
from datetime import datetime, timedelta
from functools import cached_property
from threading import Lock

from module.control.config.utils import nearest_future, dict_to_kv
from module.base.logger import logger
from module.base.exception import RequestHumanTakeover, ScriptError
from module.control.config.function import Function
from module.control.config.scheduler import TaskScheduler
from module.control.config.config_model import ConfigModel

class Config:
    def __init__(self, config_name: str, task=None) -> None:
        self.config_name = config_name
        self.waiting_tasks: list["Function"] = []
        self.waiting_tasks = TaskScheduler.priority(self.waiting_tasks)

        self.task: Optional[Function] = None  # 任务名大驼峰
        self.model = ConfigModel(config_name)

    @cached_property
    def lock_config(self) -> Lock:
        return Lock()

    def reload(self):
        """
        保存配置文件
        :return:
        """
        self.model = ConfigModel(config_name=self.config_name)

    def save(self):
        self.model.write_json(self.config_name)

    def update_scheduler(self) -> None:
        """
        更新调度器， 设置pending_task and waiting_task
        :return:
        """
        pending_task = []
        waiting_task = []
        error = []
        now = datetime.now()
        for key, value in self.model.model_dump().items():
            func = Function(key, value)

            if not func.enable:
                continue
            if not isinstance(func.next_run, datetime):
                error.append(func)
            elif func.next_run < now:
                pending_task.append(func)
            else:
                waiting_task.append(func)

        if pending_task:
            pending_task = TaskScheduler.fifo(pending_task)
        if waiting_task:
            waiting_task = sorted(
                waiting_task, key=operator.attrgetter("next_run"))

        if error:
            pending_task = error + pending_task

        self.pending_task = pending_task
        self.waiting_task = waiting_task

    def get_next(self) -> Function:
        """
        获取下一个要执行的任务
        :return:
        """
        self.update_scheduler()

        if self.pending_task:
            logger.info(f"Pending tasks: {
                [f.name for f in self.pending_task]}")
            task = self.pending_task[0]
            self.task = task
            return task

        # 哪怕是没有任务，也要返回一个任务，这样才能保证调度器正常运行
        if self.waiting_task:
            logger.info("No task pending")
            task = copy.deepcopy(self.waiting_task[0])
            logger.info(f"Waiting Task: {task}")
            return task
        else:
            logger.critical("No task waiting or pending")
            logger.critical("Please enable at least one task")
            raise RequestHumanTakeover

    def get_schedule_data(self) -> dict[str, dict]:
        """
        获取调度器的数据， 但是你必须使用update_scheduler来更新信息
        :return:
        """
        running = {}
        if self.task is not None and self.task.next_run < datetime.now():
            running = {"name": self.task.name,
                       "next_run": str(self.task.next_run)}

        pending = []
        for p in self.pending_task[1:]:
            item = {"name": p.name, "next_run": str(p.next_run)}
            pending.append(item)

        waiting = []
        for w in self.waiting_task:
            item = {"name": w.name, "next_run": str(w.next_run)}
            waiting.append(item)

        data = {"running": running, "pending": pending, "waiting": waiting}
        return data

    def task_call(self, task: str, force_call: bool = True):
        """
        回调任务，这会是在任务结束后调用
        :param task: 调用的任务的大写名称
        :param force_call: 是否强制调用任务
        :return:
        """
        task = inflection.underscore(task)
        if self.model.deep_get(self.model, keys=f'{task}.scheduler.next_run') is None:
            raise ScriptError(
                f"Task to call: {task} does not exist in user config")

        task_enable = self.model.deep_get(
            self.model, keys=f'{task}.scheduler.enable')
        if force_call or task_enable:
            logger.info(f"Task call: {task}")
            next_run = datetime.now().replace(
                microsecond=0
            )
            self.model.deep_set(self.model,
                                keys=f'{task}.scheduler.next_run',
                                value=next_run)
            self.save()
            return True
        else:
            logger.info(
                f"Task call: {task} (skipped because disabled by user)")
            return False

    def task_delay(self, task: str, start_time: Optional[datetime] = None,
                   success: bool | None = None, target_time: datetime | None = None) -> None:
        """
        设置下次运行时间  当然这个也是可以重写的
        :param target_time: 可以自定义的下次运行时间
        :param success: 判断是成功的还是失败的时间间隔
        :param task: 任务名称，大驼峰的
        :return:
        """
        # 任务预处理
        if not task:
            if not self.task:
                raise ValueError(
                    "No task provided and no current task available")
            task = self.task.name

        task = inflection.underscore(task)

        task_object = getattr(self.model, task, None)
        if not task_object:
            logger.warning(f'No task named {task}')
            return
        scheduler = getattr(task_object, 'scheduler', None)
        if not scheduler:
            logger.warning(f'No scheduler in {task}')
            return

        # 任务开始时间
        if not start_time:
            start_time = datetime.now().replace(microsecond=0)

        # 依次判断是否有自定义的下次运行时间
        run = []
        if success is not None:
            interval = (
                scheduler.success_interval
                if success
                else scheduler.failure_interval
            )
            if isinstance(interval, str):
                d, h, m, s = interval.split(":")
                interval = timedelta(days=int(d), hours=int(
                    h), minutes=int(m), seconds=int(s))
            run.append(start_time + interval)

        # # 自定义随机下次运行时间
        # run = []
        # if success is not None:
        #     m = random.randint(1, 20)
        #     s = random.randint(1, 60)
        #     interval = timedelta(minutes=m, seconds=s)
        #     run.append(start_time + interval)

        # if target_time is not None:
        #     target_time = nearest_future(target_time)
        #     run.append(target_time)

        run = min(run).replace(microsecond=0)
        next_run = run

        # 将这些连接起来，方便日志输出
        kv = dict_to_kv(
            {
                "success": success,
                "target": target_time,
            },
            allow_none=False,
        )
        logger.info(f"Delay task [{task}] to {next_run} ({kv})")

        # 保证线程安全的
        self.lock_config.acquire()
        self.lock_config.release()
        # 设置
        logger.info(f"{task}.next_run: {next_run}")


if __name__ == '__main__':
    config = Config(config_name='osa')
    config.update_scheduler()
    print(f"before: {config.get_schedule_data()}")
    print(config.get_next())

    config.task_delay('Exploration', success=True)
    print(f"after: {config.get_schedule_data()}")
    print(config.get_next())
