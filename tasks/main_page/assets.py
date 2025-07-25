from module.image_processing.rule_image import RuleImage
from module.image_processing.rule_ocr import RuleOcr
from module.image_processing.rule_swipe import RuleSwipe
from module.image_processing.rule_click import RuleClick

# This file was automatically generated by ./module/impage_processing/assets_extractor.py.
# Don't modify it manually.
class MainPageAssets: 


	# Click Rule Assets
	# 庭院头像 
	C_AVATAR = RuleClick(roi=(22, 39, 73, 59), area=(22, 39, 73, 59), name="avatar")
	# 进入游戏 
	C_ENTER_GAME = RuleClick(roi=(558, 576, 158, 38), area=(558, 576, 158, 38), name="enter_game")
	# 区域按钮 
	C_REGION = RuleClick(roi=(556, 508, 152, 34), area=(556, 508, 152, 34), name="region")
	# 退出花合战 
	C_EXIT_HUAHE = RuleClick(roi=(19, 15, 55, 48), area=(19, 15, 55, 48), name="exit_huahe")

	# Image Rule Assets
	# 用户中心 
	I_USER_CENTER = RuleImage(
		roi=(221, 449, 59, 55),
		area=(193, 421, 115, 111),
		file="./tasks/main_page/res/login/user_center.png"
	)
	# 切换账号 
	I_SWITCH_ACCOUNT = RuleImage(
		roi=(937, 180, 135, 58),
		area=(908, 151, 193, 116),
		file="./tasks/main_page/res/login/switch_account.png"
	)
	# 适龄提示 
	I_LOGIN_WARNING = RuleImage(
		roi=(165, 565, 52, 69),
		area=(0, 539, 300, 121),
		file="./tasks/main_page/res/login/login_warning.png"
	)
	# 账号登录 
	I_LOGIN = RuleImage(
		roi=(383, 413, 514, 64),
		area=(351, 381, 578, 128),
		file="./tasks/main_page/res/login/login.png"
	)
	# 苹果图标 
	I_APPLE_LOGO = RuleImage(
		roi=(511, 371, 58, 67),
		area=(482, 342, 116, 125),
		file="./tasks/main_page/res/login/apple_logo.png"
	)
	# 选择区域 
	I_PICK_REGION = RuleImage(
		roi=(500, 77, 271, 33),
		area=(484, 61, 303, 65),
		file="./tasks/main_page/res/login/pick_region.png"
	)
	# 已有角色 
	I_OWN_CHARACTERS = RuleImage(
		roi=(245, 417, 121, 29),
		area=(231, 403, 149, 57),
		file="./tasks/main_page/res/login/own_characters.png"
	)
	# 展开已有账号区域 
	I_OPEN_REGIONS = RuleImage(
		roi=(1040, 583, 20, 31),
		area=(1030, 573, 40, 51),
		file="./tasks/main_page/res/login/open_regions.png"
	)
	# 海外加速区 
	I_REGION_HAIWAI = RuleImage(
		roi=(681, 492, 64, 47),
		area=(220, 450, 830, 120),
		file="./tasks/main_page/res/regions/region_haiwai.png"
	)
	# 花火之夏 
	I_REGION_HUAHUO = RuleImage(
		roi=(276, 491, 64, 49),
		area=(220, 450, 830, 120),
		file="./tasks/main_page/res/regions/region_huahuo.png"
	)
	# 人间千年 
	I_REGION_RENJIAN = RuleImage(
		roi=(473, 494, 73, 45),
		area=(220, 450, 830, 120),
		file="./tasks/main_page/res/regions/region_renjian.png"
	)
	# 猫川别馆 
	I_REGION_MAOCHUAN = RuleImage(
		roi=(882, 492, 65, 48),
		area=(220, 450, 830, 120),
		file="./tasks/main_page/res/regions/region_maochuan.png"
	)
	# 永生之海 
	I_REGION_YONGSHENG = RuleImage(
		roi=(711, 493, 71, 47),
		area=(220, 450, 830, 120),
		file="./tasks/main_page/res/regions/region_yongsheng.png"
	)
	# 神之晚宴 
	I_REGION_SHENZHI = RuleImage(
		roi=(916, 492, 65, 48),
		area=(220, 450, 830, 120),
		file="./tasks/main_page/res/regions/region_shenzhi.png"
	)
	# 有龙则灵 
	I_REGION_YOULONG = RuleImage(
		roi=(919, 488, 63, 51),
		area=(220, 450, 830, 120),
		file="./tasks/main_page/res/regions/region_youlong.png"
	)

	# Image Rule Assets
	# 邮件 
	I_MAIL = RuleImage(
		roi=(248, 506, 40, 20),
		area=(238, 496, 60, 40),
		file="./tasks/main_page/res/mail/mail.png"
	)
	# 邮件入口 
	I_MAIL_ENT = RuleImage(
		roi=(1135, 32, 39, 27),
		area=(1121, 18, 67, 55),
		file="./tasks/main_page/res/mail/mail_ent.png"
	)
	# 未读邮件 
	I_UNREAD_MAIL = RuleImage(
		roi=(166, 132, 49, 40),
		area=(112, 77, 156, 588),
		file="./tasks/main_page/res/mail/unread_mail.png"
	)
	# 邮件标题 
	I_MAIL_HEADER = RuleImage(
		roi=(582, 49, 113, 36),
		area=(564, 31, 149, 72),
		file="./tasks/main_page/res/mail/mail_header.png"
	)
	# 全部领取邮件 
	I_GET_ALL_MAIL = RuleImage(
		roi=(89, 617, 64, 56),
		area=(61, 589, 120, 112),
		file="./tasks/main_page/res/mail/get_all_mail.png"
	)
	# 全部领取确定 
	I_MAIL_CONFIRM = RuleImage(
		roi=(685, 545, 172, 57),
		area=(657, 517, 228, 113),
		file="./tasks/battle/res/battle_fight_again_confirm.png"
	)
	# 退出邮件窗口 
	I_MAIL_EXIT = RuleImage(
		roi=(1155, 93, 46, 46),
		area=(1132, 70, 92, 92),
		file="./tasks/general/res/buttons/b_red_x.png"
	)
	# 菜单绘卷关闭 
	I_SCROLL_CLOSE = RuleImage(
		roi=(1179, 637, 36, 27),
		area=(1161, 624, 72, 54),
		file="./tasks/main_page/res/scroll_close.png"
	)
	# 菜单绘卷开启 
	I_SCROLL_OPEN = RuleImage(
		roi=(1207, 609, 33, 83),
		area=(1190, 568, 66, 166),
		file="./tasks/main_page/res/scroll_open.png"
	)
	# 商店礼包屋入口 
	I_STORE_PACK = RuleImage(
		roi=(1140, 647, 62, 38),
		area=(1109, 628, 124, 76),
		file="./tasks/main_page/res/store/store_pack.png"
	)
	# 商店礼包推荐灯笼 
	I_STORE_REC = RuleImage(
		roi=(1195, 194, 28, 58),
		area=(1172, 50, 70, 350),
		file="./tasks/main_page/res/store/store_rec.png"
	)
	# 商店每日签到奖励 
	I_STORE_DAILY_REWARD = RuleImage(
		roi=(251, 164, 280, 103),
		area=(111, 112, 560, 206),
		file="./tasks/main_page/res/store/store_daily_reward.png"
	)
	# 商店礼包屋退出 
	I_STORE_EXIT = RuleImage(
		roi=(16, 7, 44, 40),
		area=(0, 0, 88, 80),
		file="./tasks/main_page/res/store/store_exit.png"
	)
	# 花合战 
	I_HUAHE = RuleImage(
		roi=(765, 614, 63, 44),
		area=(743, 592, 107, 88),
		file="./tasks/main_page/res/huahe.png"
	)
	# 好友 
	I_FRIENDS = RuleImage(
		roi=(889, 626, 42, 46),
		area=(868, 605, 84, 88),
		file="./tasks/main_page/res/friends/friends.png"
	)
	# 好友标题 
	I_FRIEND_HEADER = RuleImage(
		roi=(586, 48, 145, 36),
		area=(568, 30, 181, 72),
		file="./tasks/main_page/res/friends/friend_header.png"
	)
	# 友情点/灰 
	I_FRIEND_POINTS = RuleImage(
		roi=(151, 643, 30, 38),
		area=(136, 628, 60, 68),
		file="./tasks/main_page/res/friends/friend_points.png"
	)
	# 友情点/亮 
	I_FRIEND_POINTS_ENABLE = RuleImage(
		roi=(128, 633, 60, 51),
		area=(102, 607, 112, 103),
		file="./tasks/main_page/res/friends/friend_points_enable.png"
	)
	# 跨区好友 
	I_CROSS_REGION_FRIENDS = RuleImage(
		roi=(240, 582, 99, 22),
		area=(229, 571, 121, 44),
		file="./tasks/main_page/res/friends/cross_region_friends.png"
	)
	# 一键收取 
	I_GET_ALL_FRIEND_POINTS = RuleImage(
		roi=(50, 541, 136, 44),
		area=(28, 519, 180, 88),
		file="./tasks/main_page/res/friends/get_all_friend_points.png"
	)
	# 好友羁绊提升关闭 
	I_FRIEND_LEVEL_UP_CLOSE = RuleImage(
		roi=(1138, 72, 46, 46),
		area=(1115, 49, 92, 92),
		file="./tasks/general/res/buttons/b_red_x.png"
	)
	# 退出好友 
	I_FRIENDS_EXIT = RuleImage(
		roi=(1157, 94, 46, 46),
		area=(1134, 71, 92, 92),
		file="./tasks/general/res/buttons/b_red_x.png"
	)
	# 签到 
	I_SIGN = RuleImage(
		roi=(253, 509, 24, 20),
		area=(243, 499, 44, 40),
		file="./tasks/main_page/res/sign.png"
	)
	# 每日一签 
	I_DAILY_SIGN = RuleImage(
		roi=(597, 165, 87, 194),
		area=(553, 121, 175, 282),
		file="./tasks/main_page/res/daily_sign.png"
	)
	# 签到页面纸人 
	I_SIGN_DOLL = RuleImage(
		roi=(843, 538, 39, 120),
		area=(823, 518, 79, 160),
		file="./tasks/main_page/res/sign_doll.png"
	)
	# 关闭每日签到 
	I_CLOSE_DAILY_SIGN = RuleImage(
		roi=(849, 87, 46, 46),
		area=(826, 64, 92, 92),
		file="./tasks/general/res/buttons/b_red_x.png"
	)
	# 每日勾玉领取 
	I_DAILY_JADE = RuleImage(
		roi=(734, 482, 31, 34),
		area=(718, 466, 63, 66),
		file="./tasks/main_page/res/daily_jade.png"
	)
	# 每日寿司 
	I_DAILY_EP = RuleImage(
		roi=(737, 489, 26, 28),
		area=(724, 476, 52, 54),
		file="./tasks/main_page/res/daily_ep.png"
	)
	# 寮礼包 
	I_GUILD_PACK = RuleImage(
		roi=(246, 502, 34, 34),
		area=(229, 485, 68, 68),
		file="./tasks/main_page/res/guild_pack.png"
	)
	# 花合战 
	I_HUAHE = RuleImage(
		roi=(782, 614, 46, 44),
		area=(760, 592, 90, 88),
		file="./tasks/main_page/res/huahe.png"
	)
	# 全部领取花合战 
	I_GET_ALL_HUAHE = RuleImage(
		roi=(912, 604, 57, 55),
		area=(884, 576, 113, 111),
		file="./tasks/main_page/res/get_all_huahe.png"
	)
	# 获得奖励 
	I_HUAHE_GAIN_REWARD = RuleImage(
		roi=(476, 233, 329, 42),
		area=(400, 160, 500, 170),
		file="./tasks/general/res/gain_reward.png"
	)
	# 每日御魂觉醒加成包 
	I_DAILY_BUFF = RuleImage(
		roi=(251, 502, 27, 33),
		area=(237, 488, 55, 61),
		file="./tasks/main_page/res/daily_buff.png"
	)
	# 商店礼包推荐 
	I_SHOP_PACK = RuleImage(
		roi=(252, 497, 32, 39),
		area=(250, 500, 60, 70),
		file="./tasks/main_page/res/shop_pack.png"
	)
	# 关闭商店礼包推荐 
	I_SHOP_PACK_CLOSE = RuleImage(
		roi=(950, 165, 46, 46),
		area=(927, 142, 92, 92),
		file="./tasks/general/res/buttons/b_red_x.png"
	)

	# Image Rule Assets
	# 悬赏封印 
	I_QUEST = RuleImage(
		roi=(235, 337, 44, 34),
		area=(100, 270, 320, 168),
		file="./tasks/main_page/res/quest/quest.png"
	)
	# 悬赏封印标题 
	I_QUEST_HEADER = RuleImage(
		roi=(572, 62, 170, 38),
		area=(553, 43, 208, 76),
		file="./tasks/main_page/res/quest/quest_header.png"
	)
	# 悬赏邀请+ 
	I_QUEST_PLUS_BUTTON = RuleImage(
		roi=(143, 358, 37, 52),
		area=(125, 340, 1015, 88),
		file="./tasks/main_page/res/quest/quest_plus_button.png"
	)
	# 跨区/灰 
	I_CROSS_REGION = RuleImage(
		roi=(267, 85, 102, 57),
		area=(239, 57, 158, 113),
		file="./tasks/main_page/res/quest/cross_region.png"
	)
	# 跨区/亮 
	I_CROSS_REGION_ENABLE = RuleImage(
		roi=(266, 81, 102, 63),
		area=(234, 49, 166, 127),
		file="./tasks/main_page/res/quest/cross_region_enable.png"
	)
	# 好友头像 
	I_QUEST_AVATAR = RuleImage(
		roi=(176, 209, 29, 24),
		area=(150, 180, 580, 350),
		file="./tasks/main_page/res/quest/quest_avatar.png"
	)
	# 好友头像已选中 
	I_QUEST_AVATAR_SELECTED = RuleImage(
		roi=(178, 207, 29, 28),
		area=(150, 180, 580, 350),
		file="./tasks/main_page/res/quest/quest_avatar_selected.png"
	)
	# 邀请 
	I_INVITE = RuleImage(
		roi=(503, 543, 132, 63),
		area=(471, 511, 196, 127),
		file="./tasks/main_page/res/quest/invite.png"
	)
	# 关闭悬赏面板 
	I_CLOSE_QUEST_BOARD = RuleImage(
		roi=(1156, 113, 46, 46),
		area=(1133, 90, 92, 92),
		file="./tasks/general/res/buttons/b_red_x.png"
	)
	# 勾协邀请 
	I_QUEST_JADE = RuleImage(
		roi=(654, 459, 60, 50),
		area=(526, 420, 235, 135),
		file="./tasks/main_page/res/quest/quest_jade.png"
	)
	# 体协邀请 
	I_QUEST_EP = RuleImage(
		roi=(654, 460, 60, 47),
		area=(526, 420, 235, 135),
		file="./tasks/main_page/res/quest/quest_ep.png"
	)
	# 狗粮协作邀请 
	I_QUEST_DOG = RuleImage(
		roi=(204, 514, 64, 55),
		area=(526, 420, 235, 135),
		file="./tasks/main_page/res/quest/quest_dog.png"
	)
	# 猫粮协作邀请 
	I_QUEST_CAT = RuleImage(
		roi=(204, 515, 64, 54),
		area=(526, 420, 235, 135),
		file="./tasks/main_page/res/quest/quest_cat.png"
	)
	# 接受悬赏邀请 
	I_QUEST_ACCEPT = RuleImage(
		roi=(825, 395, 55, 46),
		area=(798, 372, 110, 92),
		file="./tasks/main_page/res/quest/quest_accept.png"
	)
	# 拒绝悬赏邀请 
	I_QUEST_REJECT = RuleImage(
		roi=(826, 495, 53, 49),
		area=(800, 470, 106, 98),
		file="./tasks/main_page/res/quest/quest_reject.png"
	)
	# 关闭/无视悬赏邀请 
	I_QUEST_IGNORE = RuleImage(
		roi=(764, 107, 40, 38),
		area=(744, 88, 80, 76),
		file="./tasks/main_page/res/quest/quest_ignore.png"
	)
	# 协作邀请现世标记位置 
	I_QUEST_VIRTUAL = RuleImage(
		roi=(524, 159, 26, 29),
		area=(511, 144, 52, 58),
		file="./tasks/main_page/res/quest/quest_virtual.png"
	)
	# 现世共享+ 
	I_VIRTUAL_INVITE = RuleImage(
		roi=(444, 360, 38, 46),
		area=(125, 340, 1015, 88),
		file="./tasks/main_page/res/quest/virtual_invite.png"
	)


	# Swipe Rule Assets
	# 已有角色往左滑 
	S_REGION_TO_LEFT = RuleSwipe(
		roi_start=(800, 470, 60, 100),
		roi_end=(400, 470, 50, 100),
		name="region_to_left"
	)


