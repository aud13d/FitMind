""""这是一个网络错误提示窗口"""""

from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QTimer, Qt, Property, QEasingCurve, QPropertyAnimation
from PySide6.QtGui import QColor

class NetworkErrorTipLabel(QLabel):
    def __init__(self, parent=None, duration=3000):
        super().__init__(parent)
        self.setStyleSheet("""
            background-color: rgba(255, 0, 0, 180);
            color: white;
            padding: 8px 15px;
            border-radius: 5px;
            font-weight: bold;
        """)
        self.setAlignment(Qt.AlignCenter)
        self.setWindowFlags(Qt.ToolTip | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self._opacity = 1.0
        self.duration = duration  # 提示显示时间，单位毫秒

        self.animation = QPropertyAnimation(self, b"opacity", self)
        self.animation.setDuration(1000)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.finished.connect(self.hide)

    def show_message(self, message):
        # 防御处理：如果是列表，转换成字符串
        if isinstance(message, list):
            msg_list = [err.get("msg", str(err)) for err in message]
            message = "\n".join(msg_list)
        elif not isinstance(message, str):
            message = str(message)

        self.setText(message)
        self.adjustSize()
        self.setWindowOpacity(1.0)
        self.show()

        QTimer.singleShot(self.duration, self.fade_out)

    def fade_out(self):
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0.0)
        self.animation.start()

    def get_opacity(self):
        return self._opacity

    def set_opacity(self, opacity):
        self._opacity = opacity
        self.setWindowOpacity(opacity)

    opacity = Property(float, get_opacity, set_opacity)

