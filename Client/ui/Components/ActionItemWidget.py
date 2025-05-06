from PySide6.QtWidgets import QFrame, QLabel, QPushButton, QHBoxLayout
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize

class ActionItemWidget(QFrame):
    def __init__(self, icon_path: str, text: str, parent=None):
        super().__init__(parent)

        self.setMinimumHeight(55)
        self.setStyleSheet("background-color: white; border-radius: 10px;")
        self.setFrameShape(QFrame.StyledPanel)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(-1, 0, -1, 0)
        layout.setSpacing(10)

        # 左侧占位 label
        self.label_left = QLabel(self)
        self.label_left.setMinimumSize(0, 0)
        layout.addWidget(self.label_left, 2)

        # 中间图标按钮
        self.button = QPushButton(self)
        self.button.setText(text)
        self.button.setIcon(QIcon(icon_path))
        self.button.setIconSize(QSize(36, 36))
        self.button.setStyleSheet("text-align: left; border: none;")
        layout.addWidget(self.button, 10)

        # 右侧占位 label
        self.label_right = QLabel(self)
        layout.addWidget(self.label_right, 2)

        self.setLayout(layout)

##使用：
# from Components.action_item import ActionItemWidget
#
# def add_action_item_to_list(layout):
#     action = ActionItemWidget(icon_path=":/icons/icon/ticao.png", text="腿部训练")
#     layout.addWidget(action)
