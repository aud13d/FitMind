"""""自定义动作标签，用来动态添加动作的载体"""""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QLabel, QPushButton, QHBoxLayout


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

        layout = QHBoxLayout(self)
        image_label = QLabel()
        image_label.setFixedSize(24, 24)
        if action_icon:
            pixmap = action_icon.pixmap(24,24)
            pixmap = pixmap.scaled(image_label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            image_label.setPixmap(pixmap)
            image_label.setStyleSheet("border-radius: 30px;")
        else:
            image_label.setStyleSheet("background-color: gray; border-radius: 30px;")  # 没有图时灰色


        name_label = QLabel(action_name)
        name_label.setAlignment(Qt.AlignCenter)
        name_label.setStyleSheet("font-size: 16px;")

        settings_button = QPushButton("⚙")
        settings_button.setStyleSheet("background-color: transparent; border: none; font-size: 16px")
        settings_button.setFixedSize(32, 32)


        layout.addWidget(image_label)
        layout.addWidget(name_label)
        layout.addStretch()
        layout.addWidget(settings_button)


