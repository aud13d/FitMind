"""""这是一个动作的抽屉面板组件"""""
from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt, Signal

class ActionSettingFrame(QFrame):

    closed = Signal()  # 点击遮罩层外部时触发关闭

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(180, 240)
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border-top-right-radius: 12px;
                border-bottom-right-radius: 12px;
                border: 1px solid #ccc;
            }
            QPushButton {
                background-color: transparent;
                border: none;
                text-align: left;
                padding: 8px 12px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)

        options = [
            "Action details",
            "Set number of groups",
            "Set the number of times",
            "Set rest periods between sets",
            "Action sequencing",
            "Delete action"
        ]

        for opt in options:
            btn = QPushButton(opt)
            layout.addWidget(btn)

        self.setVisible(False)

    def close_drawer(self):
        """关闭抽屉面板"""
        self.setVisible(False)
        self.closed.emit()
