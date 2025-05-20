from datetime import datetime

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt, Signal, QDateTime
from PySide6.QtWidgets import QDialog

from Client.ui.Designer.ui_ImplementAerobic import Ui_ImplementAerobicDialog


class ImplementAerobicDialog(QDialog, Ui_ImplementAerobicDialog):
    aerobic_finished = QtCore.Signal(float, QtCore.QDateTime)
    def __init__(self, parent=None,aerobic_name="", aerobic_mode="Steady aerobic",target_time=1, interval=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        if parent:
            self.setGeometry(parent.geometry())
            self.frame.setGeometry(self.rect())

        # 添加继续与结束按钮,初始隐藏
        self.button_continue = QtWidgets.QPushButton("Resume",self)
        self.button_finish = QtWidgets.QPushButton("End",self)

        # 设置按钮大小、样式
        for btn in [self.button_continue, self.button_finish]:
            btn.setFixedSize(100, 100)
            btn.setVisible(False)
            btn.setStyleSheet("border-radius: 50px; color: black;")

        self.button_continue.setStyleSheet("background-color: rgb(30, 205, 30); border-radius: 50px; color: black;")
        self.button_finish.setStyleSheet("background-color: red; border-radius: 50px; color: black;")

        # 创建按钮区域（横向排列）
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setSpacing(20)
        self.button_layout.setAlignment(QtCore.Qt.AlignHCenter)

        # 默认只添加“开始”按钮，另外两个先不添加
        self.button_layout.addWidget(self.button_aerboic_start)

        self.aerobic_name = aerobic_name
        self.set_aerobic_name()
        self.aerobic_mode = aerobic_mode
        self.target_time = target_time
        self.interval = interval

        self.elapsed_seconds = 0
        self.is_running = False
        self.timer = QtCore.QTimer(self)
        self.set_aerobic_hint()

        self.init_layout()
        self.bind()

        # 网络请求相关
        self.start_datetime = None

    def init_layout(self):
        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        layout.setSpacing(20)

        layout.addWidget(self.label_aerobic_time, alignment=QtCore.Qt.AlignHCenter)
        layout.addWidget(self.label_aerobic_hint, alignment=QtCore.Qt.AlignHCenter)
        layout.addLayout(self.button_layout)

        self.setLayout(layout)

    def bind(self):
        self.timer.timeout.connect(self.update_time)
        self.button_aerboic_start.clicked.connect(self.start_aerobic)

        self.button_continue.clicked.connect(self.resume_aerobic)
        self.button_finish.clicked.connect(self.finish_aerobic)

    def set_aerobic_name(self):
        self.label_aerobic_name.setText(self.aerobic_name)

    def set_aerobic_state(self,text="Not started"):
        self.label_aerobic_state.setText(text)

    def set_aerobic_hint(self):
        if self.aerobic_mode == "Steady aerobic":
            self.label_aerobic_hint.setText(f"Steady aerobic,Target time: {self.target_time}min")
        elif self.aerobic_mode == "Interval spead":
            self.label_aerobic_hint.setText(f"Change speed every {self.interval} seconds")

    def start_aerobic(self):
        self.start_datetime = QDateTime.currentDateTime()  # 记录开始时间
        self.timer.start(1000)
        self.is_running = True
        self.label_aerobic_state.setText("Aerobic started")

        self.button_aerboic_start.setText("Pause")
        self.button_aerboic_start.setStyleSheet("background-color:white;color:black;border-radius: 50px;")

        # 重新绑定按钮
        self.button_aerboic_start.clicked.disconnect()
        self.button_aerboic_start.clicked.connect(self.pause_aerobic)

    def pause_aerobic(self):
        self.timer.stop()
        self.is_running = False
        self.label_aerobic_state.setText("Paused")
        self.button_aerboic_start.setVisible(False)

        base_geom = self.button_aerboic_start.geometry()
        center_x = self.width() // 2

        y = base_geom.y()
        btn_w = self.button_continue.width()
        spacing = 160  # 两个按钮中心点之间的距离

        # Resume（左）
        self.button_continue.move(center_x - spacing // 2 - btn_w // 2, y)
        self.button_continue.setVisible(True)

        # End（右）
        self.button_finish.move(center_x + spacing // 2 - btn_w // 2, y)
        self.button_finish.setVisible(True)

    def update_time(self):
        minutes = self.elapsed_seconds // 60
        seconds = self.elapsed_seconds % 60
        self.label_aerobic_time.setText(f"{minutes:02d}:{seconds:02d}")
        self.elapsed_seconds += 1

        if self.elapsed_seconds >= self.target_time * 60:
            self.label_aerobic_state.setText("Goal accomplished")

    def resume_aerobic(self):
        self.timer.start(1000)
        self.is_running = True
        self.label_aerobic_state.setText("Aerobic resumed")

        self.button_continue.setVisible(False)
        self.button_finish.setVisible(False)
        self.button_aerboic_start.setVisible(True)
        self.button_aerboic_start.setText("Pause")
        self.button_aerboic_start.setStyleSheet("background-color:white;color:black;border-radius: 50px;")

    def finish_aerobic(self):
        self.timer.stop()
        self.is_running = False
        self.label_aerobic_state.setText("Aerobic ended")
        self.label_aerobic_time.setStyleSheet("color: red;")

        self.button_continue.setVisible(False)
        self.button_finish.setVisible(False)
        self.button_aerboic_start.setVisible(True)
        self.button_aerboic_start.setText("Start Again")
        self.button_aerboic_start.setStyleSheet("background-color:gray;color:white;border-radius: 50px;")

        # 计算真实运动时间，秒数转float
        really_time = float(self.elapsed_seconds)

        # 发射信号，传递 really_time 和 start_datetime
        if self.start_datetime:
            self.aerobic_finished.emit(really_time, self.start_datetime)
        else:
            self.aerobic_finished.emit(really_time, QDateTime.currentDateTime())

        self.accept()  # 关闭窗口










