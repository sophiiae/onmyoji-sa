import time
from module.base.logger import logger
from module.base.exception import GamePageUnknownError
from module.base.timer import Timer
from module.image_processing.rule_image import RuleImage
from tasks.general.assets import GeneralAssets
from tasks.general.page import *
from tasks.general.page_map import PageMap
from tasks.main_page.assets import MainPageAssets
from tasks.task_base import TaskBase

class General(TaskBase, GeneralAssets, PageMap):
    ui_current: Page
    ui_close = [
        GeneralAssets.I_V_EXP_TO_MAIN, GeneralAssets.I_V_REALM_RAID_TO_EXP,
        MainPageAssets.I_STORE_EXIT, GeneralAssets.I_V_SLEEP_TO_MAIN,
        GeneralAssets.I_B_BLUE_LEFT_ANGLE, GeneralAssets.I_B_RED_X, GeneralAssets.I_B_YELLOW_LEFT_ANGLE
    ]

    def check_page_appear(self, page, check_delay: float = 0.01):
        """
        判断当前页面是否为page
        """
        time.sleep(check_delay)
        if not self.wait_until_appear(page.check_button, 1, threshold=0.95):
            logger.warning(f"Not in {page.name} page")
            return False
        return True

    def is_scroll_closed(self):
        """
        判断庭院界面卷轴是否打开
        """
        return self.appear(MainPageAssets.I_SCROLL_CLOSE)

    def get_current_page(self) -> Page:
        timeout = Timer(5, 20).start()
        logger.info("Getting current page")

        while 1:
            self.screenshot()

            # 如果20S还没有到底，那么就抛出异常
            if timeout.reached():
                break

            for page in self.MAP.keys():
                if page.check_button is None:
                    continue
                if self.check_page_appear(page=page):
                    logger.info(f"[UI]: {page.name}")
                    self.ui_current = page
                    return page

            # Try to close unknown page
            for close in self.ui_close:
                if self.wait_until_click(close):
                    logger.warning('Trying to switch to supported page')
                    timeout = Timer(5, 10).start()
                time.sleep(0.2)
        logger.critical("Starting from current page is not supported")
        raise GamePageUnknownError

    def goto(self, destination: Page, current: Page | None = None):
        if not current:
            self.get_current_page()
            current = self.ui_current

        path = self.find_path(current, destination)
        if path is None:
            logger.error(
                f"No path found from {current.name} to {destination.name}")
            return

        logger.info(f"[PATH] Start following the path: {
                    [p.name for p in path]}")

        for idx, page in enumerate(path):
            # 已经到达页面，退出
            if page == destination:
                logger.info(f'[UI] Page arrive: {destination}')
                return

            while 1:
                self.screenshot()

                if self.check_page_appear(path[idx + 1]):
                    break

                button = page.links[path[idx + 1]]
                if self.wait_until_click(button, interval=0.2):
                    logger.info(f"[PATH] Heading from {
                                page.name} to {path[idx + 1].name}.")
                    time.sleep(0.2)


# if __name__ == '__main__':
#     from pathlib import Path
#     import sys
#     sys.path.append(str(Path(__file__).parent.parent.parent))
#     from module.config.config_model import ConfigModel
#     from module.server.device import Device

#     config = ConfigModel('osa')
#     device = Device(config)

#     game = General(config, device)
#     print(game.appear(game.I_V_SLEEP_TO_MAIN))
#     print(game.exp_to_home())
#     game.goto(page_summon)
