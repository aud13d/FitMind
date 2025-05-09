"""""自定义半透明黑色遮层，用来在弹出窗口时遮住背景"""""

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
class MaskWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.FramelessWindowHint, True)  # 去掉边框
        self.setAttribute(Qt.WA_StyledBackground)  # 支持样式
        self.setAttribute(Qt.WA_DeleteOnClose)  # 关闭时自动删除

        # 获取主窗口的圆角半径
        self.corner_radius = 20

        # 设置半透明背景并应用圆角
        self.setStyleSheet(f'''
            background: rgba(0, 0, 0, 150);
            border-radius: {self.corner_radius}px;
        ''')

    def show(self):
        """显示遮罩层"""
        if self.parent() is None:
            return
        parent_rect = self.parent().geometry()
        self.setGeometry(0, 0, parent_rect.width(), parent_rect.height())
        super().show()

