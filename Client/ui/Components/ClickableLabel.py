"""""这是一个自定义的可点击Label组件"""""
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Signal

class ClickableLabel(QLabel):
    clicked = Signal()  # 自定义信号

    def mousePressEvent(self, event):
        self.clicked.emit()  # 发出点击信号
        super().mousePressEvent(event)
