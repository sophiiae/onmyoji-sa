import sys
from venv import logger

import subprocess
from module.control.emulator.close_all import kill_mumu_process
from tasks.royal_battle.task_script import TaskScript
from module.control.server.device import Device

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logger.error("Missing config name")
    else:
        name = sys.argv[1]
        d = Device(config_name=name)
        task = TaskScript(d)
        task.run()
        # kill_mumu_process()
        # subprocess.run(["shutdown", "/f", "/s", "/t", "30"])
