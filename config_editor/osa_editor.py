from config_editor.log_window import LogWindow
from config_editor.script_worker import ScriptWorker
from PyQt6.QtWidgets import QTabWidget
from config_editor.widgets.select_button import SelectButton
from config_editor.widgets.value_button import ValueButton
from config_editor.main import ConfigTab
from config_editor.sections.area_boss_section import AreaBossSection
from config_editor.sections.shikigami_activity_section import ShikigamiActivitySection
from config_editor.sections.goryou_realm_section import GoryouRealmSection
from config_editor.sections.realm_raid_section import RealmRaidSection
from config_editor.sections.exploration_section import ExplorationSection
from config_editor.sections.wanted_quests_section import WantedQuestsSection
from config_editor.sections.daily_routine_section import DailyRoutineSection
from config_editor.sections.script_section import ScriptSection
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout,
                             QWidget, QScrollArea, QCheckBox, QComboBox, QSpinBox, QLineEdit,
                             QPushButton, QHBoxLayout, QMessageBox, QLabel, QGridLayout, QGroupBox)
import sys
import os
from module.base.logger import logger

# 获取正确的配置目录路径
def get_config_dir():
    """获取配置目录的路径"""
    if getattr(sys, 'frozen', False):
        # 如果是exe环境，使用exe所在目录
        base_path = os.path.dirname(sys.executable)
    else:
        # 如果是开发环境，使用当前目录
        base_path = os.path.dirname(os.path.abspath(__file__))
        # 回到项目根目录
        base_path = os.path.dirname(base_path)

    config_dir = os.path.join(base_path, "configs")
    return config_dir


CONFIG_DIR = get_config_dir()

class OSAEditor(ConfigTab):
    def __init__(self, config_path):
        super().__init__(config_path)
        self.setWindowTitle("Onmyoji Smart Assistant")
        self.script_worker = None
        self.log_window = None
        self.current_highlighted_section = None  # 当前高亮的section
        self.highlight_timer = QTimer()  # 高亮清除定时器
        self.highlight_timer.setSingleShot(True)
        self.highlight_timer.timeout.connect(self.clear_all_highlights)
        self.setup_ui()

    def setup_ui(self):
        """设置UI界面"""
        # 主布局 - 使用水平布局来放置配置区域和日志区域
        main_layout = QHBoxLayout(self)
        main_layout.setSpacing(10)

        # 左侧配置区域
        left_widget = QWidget()
        left_widget.setStyleSheet("""
            QWidget {
                background-color: #fbfaff;
            }
        """)
        left_layout = QVBoxLayout(left_widget)

        # 创建运行按钮（将移到日志窗口内部）
        self.run_button = QPushButton("运行")
        self.run_button.setMinimumWidth(80)  # 设置最小宽度，类似状态标签
        self.run_button.setMaximumWidth(100)  # 设置最大宽度
        self.set_run_button_style()
        self.run_button.clicked.connect(self.run_osa_config)

        # 快速导航栏
        nav_widget = QWidget()
        nav_widget.setStyleSheet("""
            QWidget {
                background-color: #fbfaff;
            }
        """)
        nav_layout = QVBoxLayout(nav_widget)
        nav_layout.setContentsMargins(2, 2, 2, 2)  # 减少导航栏边距
        nav_layout.setSpacing(2)  # 减少导航栏间距

        # 创建按钮容器，使用网格布局实现自动换行
        button_container = QWidget()
        button_container.setStyleSheet("""
            QWidget {
                background-color: #fbfaff;
            }
        """)
        button_layout = QGridLayout(button_container)
        button_layout.setSpacing(3)  # 减少按钮间距
        button_layout.setContentsMargins(2, 2, 2, 2)  # 减少按钮容器边距

        # 创建导航按钮
        sections = [
            ("script", "脚本设置", None),  # 脚本设置没有启用状态
            ("daily_routine", "日常任务", "daily_routine.scheduler.enable"),
            ("wanted_quests", "悬赏任务", None),  # 悬赏任务没有启用状态
            ("exploration", "探索", "exploration.scheduler.enable"),
            ("realm_raid", "结界突破", "realm_raid.scheduler.enable"),
            ("goryou_realm", "御灵", "goryou_realm.scheduler.enable"),
            ("shikigami_activity", "式神活动", "shikigami_activity.scheduler.enable"),
            ("area_boss", "地域鬼王", "area_boss.scheduler.enable")
        ]

        # 设置统一的按钮样式
        button_style = """
            QPushButton {
                min-width: 40px;
                max-width: 50px;
                font-size: 9px;
                margin: 0px;
                padding: 2px 4px;
            }
        """

        # 计算每行最多放置的按钮数量（根据容器宽度动态调整）
        max_buttons_per_row = 7  # 增加到7个按钮一行，更紧凑

        for i, (section_id, section_name, enable_path) in enumerate(sections):
            btn = QPushButton(section_name)
            btn.setStyleSheet(button_style)  # 应用基础样式
            btn.clicked.connect(
                lambda checked, s=section_id: self.scroll_to_section(s))

            # 计算按钮在网格中的位置
            row = i // max_buttons_per_row
            col = i % max_buttons_per_row

            button_layout.addWidget(btn, row, col)
            self.nav_buttons[section_id] = (btn, enable_path)

        nav_layout.addWidget(button_container)
        left_layout.addWidget(nav_widget)

        # 滚动区域
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # 禁用水平滚动条
        scroll.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded)  # 只在需要时显示垂直滚动条

        # 设置滚动区域背景色
        scroll.setStyleSheet("""
            QScrollArea {
                background-color: #F2ECF9;
                border: none;
            }
        """)

        # 创建滚动区域的内容部件
        scroll_widget = QWidget()
        scroll_widget.setStyleSheet("""
            QWidget {
                background-color: #F2ECF9;
            }
        """)
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.setSpacing(10)  # 设置部件之间的间距
        scroll_layout.setContentsMargins(10, 10, 10, 10)  # 设置边距

        # 添加所有配置部分
        self.script_section = ScriptSection(self.config)
        scroll_layout.addWidget(self.script_section)

        self.daily_routine_section = DailyRoutineSection(self.config)
        scroll_layout.addWidget(self.daily_routine_section)

        self.wanted_quests_section = WantedQuestsSection(self.config)
        scroll_layout.addWidget(self.wanted_quests_section)

        self.exploration_section = ExplorationSection(self.config)
        scroll_layout.addWidget(self.exploration_section)

        self.realm_raid_section = RealmRaidSection(self.config)
        scroll_layout.addWidget(self.realm_raid_section)

        self.goryou_realm_section = GoryouRealmSection(self.config)
        scroll_layout.addWidget(self.goryou_realm_section)

        self.shikigami_activity_section = ShikigamiActivitySection(self.config)
        scroll_layout.addWidget(self.shikigami_activity_section)

        self.area_boss_section = AreaBossSection(self.config)
        scroll_layout.addWidget(self.area_boss_section)

        # 为所有section添加点击事件
        self.setup_section_click_events()

        # 添加弹性空间，使内容靠上
        scroll_layout.addStretch()

        # 设置滚动区域的内容
        scroll.setWidget(scroll_widget)
        left_layout.addWidget(scroll)

        # 自动保存
        self.install_auto_save()

        # 更新导航按钮状态
        self.update_nav_buttons()

        # 设置左侧配置区域的固定宽度
        left_widget.setMinimumWidth(800)  # 缩小左侧宽度
        left_widget.setMaximumWidth(450)  # 设置最大宽度

        # 添加左侧配置区域到主布局
        main_layout.addWidget(left_widget)

        # 右侧日志区域
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)

        # 创建内嵌的日志窗口，并将运行按钮传递给它
        self.log_window = LogWindow(self.get_config_name())
        self.log_window.setParent(right_widget)
        self.log_window.set_run_button(self.run_button)  # 传递运行按钮给日志窗口
        right_layout.addWidget(self.log_window)

        # 设置右侧日志区域的固定宽度
        right_widget.setMinimumWidth(500)  # 扩大右侧宽度

        # 添加右侧日志区域到主布局
        main_layout.addWidget(right_widget)

    def setup_section_click_events(self):
        """为所有配置区域设置点击事件"""
        sections = [
            self.script_section,
            self.daily_routine_section,
            self.wanted_quests_section,
            self.exploration_section,
            self.realm_raid_section,
            self.goryou_realm_section,
            self.shikigami_activity_section,
            self.area_boss_section
        ]

        for section in sections:
            # 为每个section添加鼠标点击事件
            section.mousePressEvent = lambda event, s=section: self.on_section_clicked(
                s, event)

    def on_section_clicked(self, section, event):
        """处理配置区域的点击事件"""
        # 检查是否是右键点击
        if event.button() == Qt.MouseButton.RightButton:
            self.show_highlight_menu(section, event.globalPos())
        else:
            # 左键点击：高亮被点击的section（不会清除已高亮的区域）
            self.highlight_section(section)

        # 调用原始的mousePressEvent
        QGroupBox.mousePressEvent(section, event)

    def highlight_section(self, section):
        """高亮指定的配置区域（永久保持）"""
        # 清除之前的高亮
        if self.current_highlighted_section:
            self.clear_section_highlight(self.current_highlighted_section)

        # 设置新的高亮
        if section:
            self.set_section_highlight(section)
            self.current_highlighted_section = section
            # 不启动定时器，保持永久高亮

    def highlight_section_permanent(self, section):
        """永久高亮指定的配置区域（不自动清除）"""
        # 清除之前的高亮
        if self.current_highlighted_section:
            self.clear_section_highlight(self.current_highlighted_section)

        # 设置新的高亮
        if section:
            self.set_section_highlight(section)
            self.current_highlighted_section = section
            # 不启动定时器，保持永久高亮

    def highlight_section_temporary(self, section, duration=3000):
        """临时高亮指定的配置区域（可自定义时间）"""
        # 清除之前的高亮
        if self.current_highlighted_section:
            self.clear_section_highlight(self.current_highlighted_section)

        # 设置新的高亮
        if section:
            self.set_section_highlight(section)
            self.current_highlighted_section = section
            # 启动定时器，指定时间后自动清除高亮
            self.highlight_timer.start(duration)

    def clear_section_highlight(self, section):
        """清除配置区域的高亮"""
        if section:
            # 恢复到默认背景色，确保所有组件都使用统一的背景色
            # 不强制设置checkbox样式，让它使用应用的默认样式
            section.setStyleSheet("""
                QGroupBox {
                    background-color: #F2ECF9;
                }
                QGroupBox QWidget {
                    background-color: #F2ECF9;
                }
                QGroupBox QLineEdit {
                    background-color: #F2ECF9;
                }
                QGroupBox QComboBox {
                    background-color: #F2ECF9;
                }
                QGroupBox QSpinBox {
                    background-color: #F2ECF9;
                }
                QGroupBox QCheckBox {
                    background-color: #F2ECF9;
                }
                QGroupBox QPushButton {
                    background-color: #F2ECF9;
                }
                QGroupBox QLabel {
                    background-color: #F2ECF9;
                }
                QGroupBox ValueButton {
                    background-color: #F2ECF9;
                }
                QGroupBox SelectButton {
                    background-color: #F2ECF9;
                }
            """)

    def set_section_highlight(self, section):
        """设置配置区域的高亮边框"""
        if section:
            # 使用简洁的彩色边框高亮，高亮区域内所有组件使用白色背景
            highlight_style = """
                QGroupBox {
                    border: 2px solid #9b72cf;
                    border-radius: 6px;
                    background-color: #fbfaff;
                    margin: 1px;
                    padding: 3px;
                }
                QGroupBox::title {
                    color: #9b72cf;
                    subcontrol-origin: margin;
                    left: 10px;
                    padding: 0 5px 0 5px;
                }
                QGroupBox QWidget {
                    background-color: #ffffff;
                }
                QGroupBox QLineEdit {
                    background-color: #ffffff;
                }
                QGroupBox QComboBox {
                    background-color: #ffffff;
                }
                QGroupBox QSpinBox {
                    background-color: #ffffff;
                }
                QGroupBox QCheckBox {
                    background-color: #ffffff;
                }
                QCheckBox::indicator:unchecked {
                    border: 1px solid #aa66cc;
                    background-color: white;
                    border-radius: 4px;
                }
                QCheckBox::indicator:checked {
                    background-color: #aa66cc;
                    border: 1px solid #aa66cc;
                    border-radius: 4px;
                }
                QGroupBox QPushButton {
                    background-color: #ffffff;
                }
                QGroupBox QLabel {
                    background-color: #ffffff;
                }
                QGroupBox ValueButton {
                    background-color: #ffffff;
                }
                QGroupBox SelectButton {
                    background-color: #ffffff;
                }
            """
            section.setStyleSheet(highlight_style)

    def clear_all_highlights(self):
        """清除所有高亮"""
        if self.current_highlighted_section:
            self.clear_section_highlight(self.current_highlighted_section)
            self.current_highlighted_section = None
        # 停止定时器
        self.highlight_timer.stop()

    def closeEvent(self, a0):
        """窗口关闭时的处理"""
        if self.script_worker and self.script_worker.isRunning():
            self.script_worker.terminate()
            self.script_worker.wait()

        # 停止日志捕获
        if self.log_window:
            self.log_window.stop_log_capture()

        if a0:
            a0.accept()
        super().closeEvent(a0)

    def save_osa_config(self):
        self.script_section.update_config()
        self.daily_routine_section.update_config()
        self.wanted_quests_section.update_config()
        self.exploration_section.update_config()
        self.realm_raid_section.update_config()
        self.goryou_realm_section.update_config()
        self.shikigami_activity_section.update_config()
        self.area_boss_section.update_config()
        self.save_config()

    def run_osa_config(self):
        """运行当前配置"""
        try:
            if not self.is_running:
                # 保存当前配置
                self.save_osa_config()

                # 清空旧的日志
                if self.log_window:
                    self.log_window.clear_log()

                # 获取配置名称（文件名去掉.json后缀）
                config_name = os.path.splitext(
                    os.path.basename(self.config_path))[0]

                # 创建工作线程
                self.script_worker = ScriptWorker(config_name, self.log_window)
                self.script_worker.finished.connect(self.on_script_finished)
                self.script_worker.error.connect(self.on_script_error)

                # 直接启动线程和脚本
                self.script_worker.start()

                # 更新UI状态
                self.is_running = True
                self.update_run_button()
            else:
                # 直接强制终止脚本
                self.stop_script()

        except Exception as e:
            QMessageBox.critical(self, "错误", f"运行配置时出错: {str(e)}")

    def stop_script(self):
        """停止脚本运行"""
        if self.script_worker and self.script_worker.isRunning():
            # 直接强制终止
            logger.critical("强制终止脚本")
            self.script_worker.force_stop()
            self.script_worker.terminate()
            self.script_worker.wait(100)  # 只等待100ms

        # 停止日志捕获
        if self.log_window:
            self.log_window.stop_log_capture()

        # 立即更新UI状态
        self.is_running = False
        self.update_run_button()

    def on_script_finished(self):
        """脚本完成时的回调"""
        # 停止日志捕获
        if self.log_window:
            self.log_window.stop_log_capture()

        self.is_running = False
        self.update_run_button()
        self.script_worker = None

    def on_script_error(self, error_msg):
        """脚本出错时的回调"""
        # 停止日志捕获
        if self.log_window:
            self.log_window.stop_log_capture()

        self.is_running = False
        self.update_run_button()
        self.script_worker = None
        QMessageBox.critical(self, "错误", f"脚本运行出错: {error_msg}")

    def set_run_button_style(self):
        if self.is_running:
            self.run_button.setStyleSheet("""
                QPushButton {
                    padding: 3px 8px;
                    border-radius: 3px;
                    background-color: #e63946;
                    color: white;
                    font-size: 12px;
                    min-width: 40px;
                }   
            """)
        else:
            self.run_button.setStyleSheet("""
                QPushButton {
                    padding: 3px 8px;
                    border-radius: 3px;
                    background-color: #6a994e;
                    color: white;
                    font-size: 12px;
                    min-width: 40px;
                }
            """)

    def update_run_button(self):
        """更新运行按钮的样式和文本"""
        if self.is_running:
            self.run_button.setText("停止")
        else:
            self.run_button.setText("运行")
        self.set_run_button_style()

    def install_auto_save(self):
        # 给所有控件加信号，内容变动时自动保存
        for section in [self.script_section, self.daily_routine_section, self.wanted_quests_section,
                        self.exploration_section, self.realm_raid_section, self.goryou_realm_section,
                        self.shikigami_activity_section, self.area_boss_section]:
            for child in section.findChildren((QCheckBox, QComboBox, QSpinBox, QLineEdit, ValueButton, SelectButton)):
                if hasattr(child, 'textChanged'):
                    child.textChanged.connect(self.on_config_changed)
                if hasattr(child, 'currentIndexChanged'):
                    child.currentIndexChanged.connect(self.on_config_changed)
                if hasattr(child, 'stateChanged'):
                    child.stateChanged.connect(self.on_config_changed)
                if hasattr(child, 'valueChanged'):
                    child.valueChanged.connect(self.on_config_changed)

    def on_config_changed(self):
        """配置改变时的处理函数"""
        self.save_osa_config()
        self.update_nav_buttons()

    def scroll_to_section(self, section_id):
        """滚动到指定的配置部分"""
        section_map = {
            "script": self.script_section,
            "daily_routine": self.daily_routine_section,
            "wanted_quests": self.wanted_quests_section,
            "exploration": self.exploration_section,
            "realm_raid": self.realm_raid_section,
            "goryou_realm": self.goryou_realm_section,
            "shikigami_activity": self.shikigami_activity_section,
            "area_boss": self.area_boss_section
        }

        if section_id in section_map:
            section = section_map[section_id]
            # 获取滚动区域
            scroll_area = self.findChild(QScrollArea)
            if scroll_area:
                scroll_area.ensureWidgetVisible(section)
                # 高亮选中的配置区域
                self.highlight_section(section)

    def show_highlight_menu(self, section, pos):
        """显示高亮选项菜单"""
        from PyQt6.QtWidgets import QMenu
        from PyQt6.QtGui import QAction

        menu = QMenu(self)

        # 永久高亮选项（默认）
        permanent_action = QAction("永久高亮", self)
        permanent_action.triggered.connect(
            lambda: self.highlight_section_permanent(section))
        menu.addAction(permanent_action)

        # 临时高亮选项
        temp_action = QAction("临时高亮 (10秒)", self)
        temp_action.triggered.connect(
            lambda: self.highlight_section_temporary(section, 10000))
        menu.addAction(temp_action)

        # 清除高亮选项
        clear_action = QAction("清除高亮", self)
        clear_action.triggered.connect(self.clear_all_highlights)
        menu.addAction(clear_action)

        # 显示菜单
        menu.exec(pos)
