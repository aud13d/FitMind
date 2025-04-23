from PySide6.QtCore import Qt, Signal, QTime, QTimer
from Client.ui.Designer.ui_NewTrain import Ui_Widget_NewTrain
from PySide6.QtWidgets import QWidget
from Client.ui.Components.MaskWidget import MaskWidget
from Client.ui.Logic.CancelTrainingDialog import CancelTrainingDialog
from Client.ui.Logic.FinishTrainingDialog import FinishTrainingDialog

class NewTrainWidget(QWidget):
    minimized_signal = Signal()  # 发送信号给 MainInterfaceWindow

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget_NewTrain()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.timer = QTimer(self)  # 创建定时器
        self.time = QTime(0, 0)  # 计时初始时间设为00:00
        self.timer_running = False

        self.bind()

    def bind(self):
        self.ui.button_newtrain_minimize.clicked.connect(self.minisize_window)

        self.ui.button_newtrain_start.clicked.connect(self.start_timer)
        self.timer.timeout.connect(self.update_time) # 每秒更新时间

        self.ui.button_newtrain_finish.clicked.connect(self.finish_training)

    def minisize_window(self):
        """最小化窗口并发送信号"""
        self.hide()
        self.minimized_signal.emit()  # 通知 MainInterfaceWindow

    def start_timer(self):
        """开始计时"""
        self.timer.start(1000)
        self.timer_running = True
        self.ui.button_newtrain_start.setEnabled(False)
        self.ui.button_newtrain_start.setVisible(False)
        self.ui.label_newtrain_time.setStyleSheet("color: blue;font: 700 18pt '微软雅黑';")

    def update_time(self):
        """更新时间"""
        self.time = self.time.addSecs(1)
        self.ui.label_newtrain_time.setText(self.time.toString("mm:ss"))

    def stop_timer(self):
        """停止计时并记录当前时间"""
        if not self.timer_running:
            return

        self.timer.stop()
        current_time = self.time.toString("mm:ss")
        print(f"计时结束，当前时间是: {current_time}")
        self.timer_running = False
        self.ui.button_newtrain_start.setEnabled(True)
        self.ui.button_newtrain_start.setVisible(True)

        self.ui.label_newtrain_time.setStyleSheet("color: black;font: 700 18pt '微软雅黑';")

    def finish_training(self):
        """完成训练"""
        self.open_FinishTraining()

    def open_FinishTraining(self):
        """完成训练：完成"""
        # 创建遮罩层
        self.mask = MaskWidget(self)
        self.mask.show()

        # 创建并显示对话框
        self.dialog= FinishTrainingDialog(self)
        self.dialog.setModal(True)
        self.dialog.show()
        self.dialog.raise_()
        self.dialog.exec_()

        # 关闭遮罩层
        self.mask.close()

    def open_CancelTraining(self):
        """完成训练：取消"""
        # 创建遮罩层
        self.mask = MaskWidget(self)
        self.mask.show()

        # 创建并显示对话框
        self.dialog= CancelTrainingDialog(self)
        self.dialog.setModal(True)
        self.dialog.show()
        self.dialog.raise_()
        self.dialog.exec_()

        # 关闭遮罩层
        self.mask.close()





