from PySide6.QtWidgets import QFrame
from PySide6.QtCore import Signal, Qt

class ClickableFrame(QFrame):
    clicked = Signal()  # 自定义点击信号

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)
