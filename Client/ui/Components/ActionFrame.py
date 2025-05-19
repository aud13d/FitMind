"""""自定义动作标签，用来动态添加动作的载体"""""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QLabel, QPushButton, QHBoxLayout

from Client.ui.Components.AcationSettingFrame import ActionSettingFrame
from Client.ui.Components.MaskWidget import MaskWidget


class ActionFrame(QFrame):
    def __init__(self, action_name, action_icon=None ,parent=None):
        super().__init__(parent)
        self.setObjectName("actionFrame")
        self.setStyleSheet("""
            QFrame#actionFrame {
                background-color: white;
                border-top-right-radius:15px;
                border-top-left-radius:15px;
                border-bottom-right-radius:15px;
                border-bottom-left-radius:15px;
            }
        """)
        self.setMinimumHeight(55)
        self.setMinimumWidth(335)

        # 运动属性
        self.name = action_name  # 动作名称
        self.sets = 3            # 默认组数
        self.reps = 10           # 默认每组次数
        self.note = ""           # 默认备注（空）
        self.rest_time = 1       # 默认休息时间（1分钟）
        self.order = 0           # 动作顺序

        # 运动UI元素
        layout = QHBoxLayout(self)
        image_label = QLabel()
        image_label.setFixedSize(24, 24)
        if action_icon:
            pixmap = action_icon.pixmap(24,24)
            pixmap = pixmap.scaled(image_label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            image_label.setPixmap(pixmap)
            image_label.setStyleSheet("background-color: transparent;border-radius: 30px;")
        else:
            image_label.setStyleSheet("background-color: gray; border-radius: 30px;")

        name_label = QLabel(action_name)
        name_label.setAlignment(Qt.AlignCenter)
        name_label.setStyleSheet("background-color: transparent;font-size: 16px;")

        self.settings_button = QPushButton("⚙")
        self.settings_button.setStyleSheet("background-color: transparent; border: none; font-size: 16px")
        self.settings_button.setFixedSize(32, 32)

        layout.addWidget(image_label)
        layout.addWidget(name_label)
        layout.addStretch()
        layout.addWidget(self.settings_button)




    # def complete_action(self):
    #     """完成当前动作：记录时间，更新颜色，显示持续时间"""
    #     if self.timer.isValid():
    #         duration_ms = self.timer.elapsed()
    #         duration_sec = round(duration_ms / 1000)
    #         self.duration_label.setText(f"时长：{duration_sec} 秒")
    #         self.duration_label.show()
    #
    #     self.setStyleSheet("""
    #         QFrame#actionFrame {
    #             background-color: #d4f4d7;  /* 绿色背景，表示完成 */
    #             border-radius: 15px;
    #         }
    #     """)


