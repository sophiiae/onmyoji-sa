import random
import time
from module.base.logger import logger
from module.base.timer import Timer
from module.config.enums import BuffClass
from module.image_processing.rule_image import RuleImage
from tasks.battle.assets import BattleAssets
from tasks.buff.buff import Buff
from tasks.general.page import Page
from tasks.general.general import General
from tasks.general.page import page_main

class Battle(General, Buff, BattleAssets):

    def run_easy_battle(self, exit_battle_check: RuleImage, failed_check: RuleImage | None = None) -> bool:
        logger.info("Start easy battle process")

        win = True
        action_click = random.choice(
            [self.C_REWARD_1, self.C_REWARD_2])

        while 1:
            self.wait_and_shot(0.4)
            if self.appear(exit_battle_check, 0.95):
                break

            if self.appear(self.I_REWARD):
                self.get_reward()
                win = True
                continue

            if self.appear(self.I_BATTLE_WIN, 0.95):
                self.click(action_click)
                win = True
                continue

            if failed_check and self.appear(failed_check, 0.95):
                self.click(action_click)
                win = False
            elif self.appear(self.I_BATTLE_FAILED, 0.95):
                self.click(action_click)
                win = False
        logger.info(f"** Got battle result: {win}")
        return win

    def run_battle(self) -> bool:
        # 有的时候是长战斗，需要在设置stuck检测为长战斗
        # 但是无需取消设置，因为如果有点击或者滑动的话 handle_control_check会自行取消掉
        self.device.stuck_record_add('BATTLE_STATUS_S')
        self.device.click_record_clear()

        # 战斗过程 随机点击和滑动 防封
        logger.info("Start battle process")
        win = False

        while 1:
            self.wait_and_shot()
            if self.appear(self.I_BATTLE_WIN) or self.appear(self.I_REWARD):
                win = True
                break

            if self.appear(self.I_BATTLE_FIGHT_AGAIN):
                break

        logger.info(f"** Got battle result: {win}")
        if not win:
            action_click = random.choice(
                [self.C_WIN_1, self.C_WIN_2, self.C_WIN_3, self.C_WIN_4])
            self.click(action_click)
            return win

        logger.info("Get reward")
        timeout = Timer(5, 5).start()
        got_reward = False
        while 1:
            if timeout.reached():
                break

            self.screenshot()
            if got_reward and not self.appear(self.I_REWARD):
                break

            if self.appear(self.I_REWARD):
                self.get_reward()
                got_reward = True
                continue

            if self.appear(self.I_BATTLE_WIN):
                action_click = random.choice(
                    [self.C_REWARD_1, self.C_REWARD_2])
                self.click(action_click)

        time.sleep(1)
        return win

    def get_reward(self):
        """领奖励
        """
        action_click = random.choice(
            [self.C_REWARD_1, self.C_REWARD_2])
        while 1:
            self.screenshot()
            if not self.appear(self.I_REWARD):
                break

            if self.appear(self.I_REWARD):
                self.click(action_click)

    def run_battle_quit(self):
        """
        进入挑战然后直接退出
        :param config:
        :return:
        """
        # 退出
        while 1:
            time.sleep(1)
            self.screenshot()
            if self.appear(self.I_BATTLE_FIGHT_AGAIN):
                break

            if self.appear_then_click(self.I_BATTLE_EXIT):
                self.appear_then_click(self.I_BATTLE_EXIT_CONFIRM)
                continue

        logger.info("Clicked exit battle confirm")
        while 1:
            time.sleep(0.5)
            self.screenshot()
            if self.appear(self.I_BATTLE_FIGHT_AGAIN):
                action_click = random.choice(
                    [self.C_WIN_1, self.C_WIN_2, self.C_WIN_3, self.C_WIN_4])
                self.click(action_click)
                continue
            if not self.appear(self.I_BATTLE_FIGHT_AGAIN):
                break

        return True

    def exit_battle(self) -> bool:
        self.screenshot()

        if not self.appear(self.I_BATTLE_EXIT):
            return False

        # 点击返回
        logger.info(f"Click {self.I_BATTLE_EXIT.name}")
        while 1:
            time.sleep(0.2)
            self.screenshot()
            if self.appear_then_click(self.I_BATTLE_EXIT):
                continue
            if self.appear(self.I_BATTLE_EXIT_CONFIRM):
                break

        # 点击返回确认
        while 1:
            time.sleep(0.2)
            self.screenshot()
            if self.appear_then_click(self.I_BATTLE_EXIT_CONFIRM):
                continue
            if self.appear_then_click(self.I_BATTLE_FAILED):
                continue
            if not self.appear(self.I_BATTLE_EXIT):
                break

        return True

    def check_buff(self, buff: list[BuffClass] = [], page: Page = page_main):
        if not buff:
            return

        match_buff = {
            BuffClass.AWAKE: (self.awake, True),
            BuffClass.SOUL: (self.soul, True),
            BuffClass.GOLD_50: (self.gold_50, True),
            BuffClass.GOLD_100: (self.gold_100, True),
            BuffClass.EXP_50: (self.exp_50, True),
            BuffClass.EXP_100: (self.exp_100, True),
            BuffClass.AWAKE_CLOSE: (self.awake, False),
            BuffClass.SOUL_CLOSE: (self.soul, False),
            BuffClass.GOLD_50_CLOSE: (self.gold_50, False),
            BuffClass.GOLD_100_CLOSE: (self.gold_100, False),
            BuffClass.EXP_50_CLOSE: (self.exp_50, False),
            BuffClass.EXP_100_CLOSE: (self.exp_100, False),
        }

        self.open_buff(page)
        for b in buff:
            func, activate = match_buff[b]
            func(activate)
            time.sleep(0.1)

        logger.info(f'Open buff success')
        self.close_buff()

    def toggle_team_lock(self, team_lock: RuleImage, team_unlock: RuleImage, lock: bool = True):
        # 不锁定队伍
        if not lock:
            if self.appear(team_unlock):
                return

            if self.wait_until_appear(team_lock, 1):
                self.wait_until_click(team_lock)
                logger.info("Unlock the team")
                return

        # 锁定队伍
        if lock:
            if self.appear(team_lock):
                return

            if self.wait_until_appear(team_unlock, 1):
                self.wait_until_click(team_unlock)
                logger.info("Lock the team")
                return

    def toggle_battle_auto(self):
        while 1:
            time.sleep(0.6)
            self.screenshot()
            if self.appear(self.I_BATTLE_AUTO):
                break

            if self.appear(self.I_BATTLE_MANUAL):
                self.click(self.I_BATTLE_MANUAL)
                continue

            if self.appear(self.I_BATTLE_WIN, 0.95):
                break
