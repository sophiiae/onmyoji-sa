from module.image_processing.rule_image import RuleImage
from module.image_processing.rule_ocr import RuleOcr
from module.image_processing.rule_swipe import RuleSwipe
from module.image_processing.rule_click import RuleClick

# This file was automatically generated by ./module/impage_processing/assets_extractor.py.
# Don't modify it manually.
class BattleAssets: 

	# Image Rule Assets
	# 战斗准备 
	I_BATTLE_READY = RuleImage(
		roi=(1135, 565, 87, 46),
		area=(1112, 542, 133, 92),
		file="./tasks/battle/res/battle_ready.png"
	)
	# 战斗胜利图标 
	I_BATTLE_WIN = RuleImage(
		roi=(411, 122, 172, 129),
		area=(325, 58, 344, 258),
		file="./tasks/battle/res/battle_win.png"
	)
	# 战斗失败图标 
	I_BATTLE_FAILED = RuleImage(
		roi=(409, 136, 125, 100),
		area=(359, 86, 225, 200),
		file="./tasks/battle/res/battle_failed.png"
	)
	# 探索战斗鬼火总量 
	I_BATTLE_CHECK = RuleImage(
		roi=(557, 688, 28, 26),
		area=(544, 675, 54, 52),
		file="./tasks/battle/res/battle_check.png"
	)
	# 突破战斗退出 
	I_BATTLE_EXIT = RuleImage(
		roi=(21, 17, 35, 33),
		area=(4, 0, 70, 66),
		file="./tasks/battle/res/battle_exit.png"
	)
	# 退出战斗确认 
	I_BATTLE_EXIT_CONFIRM = RuleImage(
		roi=(679, 396, 124, 52),
		area=(653, 370, 176, 104),
		file="./tasks/battle/res/battle_exit_confirm.png"
	)
	# 再次挑战 
	I_BATTLE_FIGHT_AGAIN = RuleImage(
		roi=(827, 476, 63, 72),
		area=(796, 440, 126, 144),
		file="./tasks/battle/res/battle_fight_again.png"
	)
	# 再次挑战确认 
	I_BATTLE_FIGHT_AGAIN_CONFIRM = RuleImage(
		roi=(672, 403, 172, 57),
		area=(586, 374, 344, 114),
		file="./tasks/battle/res/battle_fight_again_confirm.png"
	)
	# 战斗金币奖励 
	I_BATTLE_GOLD = RuleImage(
		roi=(266, 176, 101, 71),
		area=(230, 140, 840, 300),
		file="./tasks/battle/res/battle_gold.png"
	)
	# 手动 
	I_BATTLE_MANUAL = RuleImage(
		roi=(35, 647, 27, 28),
		area=(21, 633, 55, 56),
		file="./tasks/battle/res/battle_manual.png"
	)
	# 自动 
	I_BATTLE_AUTO = RuleImage(
		roi=(39, 647, 21, 29),
		area=(29, 637, 41, 49),
		file="./tasks/battle/res/battle_auto.png"
	)


	# Click Rule Assets
	# top left 
	C_WIN_1 = RuleClick(roi=(30, 130, 170, 110), area=(30, 130, 170, 110), name="win_1")
	# top right 
	C_WIN_2 = RuleClick(roi=(990, 70, 240, 150), area=(990, 70, 240, 150), name="win_2")
	# bottom left 
	C_WIN_3 = RuleClick(roi=(20, 550, 180, 70), area=(20, 550, 180, 70), name="win_3")
	# bottom right 
	C_WIN_4 = RuleClick(roi=(1070, 550, 200, 150), area=(1070, 550, 200, 150), name="win_4")
	# left 
	C_REWARD_1 = RuleClick(roi=(110, 130, 130, 500), area=(110, 130, 130, 500), name="reward_1")
	# right 
	C_REWARD_2 = RuleClick(roi=(1100, 130, 130, 500), area=(1100, 130, 130, 500), name="reward_2")
	# left 
	C_GAIN_REWARD_1 = RuleClick(roi=(30, 100, 270, 550), area=(30, 100, 270, 550), name="gain_reward_1")
	# right 
	C_GAIN_REWARD_2 = RuleClick(roi=(980, 120, 280, 530), area=(980, 120, 280, 530), name="gain_reward_2")
	# description 
	C_BATTLE_1 = RuleClick(roi=(130,90,400,90), area=(130,90,400,90), name="battle_1")
	# description 
	C_BATTLE_2 = RuleClick(roi=(1100,60,100,140), area=(1100,60,100,140), name="battle_2")


