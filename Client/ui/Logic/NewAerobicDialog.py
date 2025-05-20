from PySide6 import QtCore
from PySide6.QtCore import QDate, Qt, QDateTime
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QDialog, QApplication
)
from datetime import datetime
from Client.config import TypeSelectionNewAerobicDialog_IconPath, TimeSettingNewAerobicDialog_IconPath
from Client.services.user_session import UserSession
from Client.ui.Components.MaskWidget import MaskWidget
from Client.ui.Components.NetworkErrorTipLabel import NetworkErrorTipLabel
from Client.ui.Designer.ui_NewAerobic import Ui_NewAerobicDialog
from Client.ui.Components.TypeSelectionDialog import TypeSelectionDialog
from Client.ui.Components.DateDialog import DateDialog
from Client.ui.Components.TimeSettingDialog import TimeSettingDialog
from Client.services.server_aerobic import AerobicService
import json

from Client.ui.Logic.ImplementAerobicDialog import ImplementAerobicDialog


class NewAerobicDialog(QDialog, Ui_NewAerobicDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        if parent:
            self.setGeometry(parent.geometry())

        # 初始化图标
        icon_pixmap_typeSelection = QPixmap(TypeSelectionNewAerobicDialog_IconPath)
        typeSelection = icon_pixmap_typeSelection.scaled(16, 16, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.icon_type_selection.setPixmap(typeSelection)

        icon_pixmap_dateSetting = QPixmap(TimeSettingNewAerobicDialog_IconPath)
        dateSetting = icon_pixmap_dateSetting.scaled(16, 16, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.icon_time_setting.setPixmap(dateSetting)
        self.icon_training_date.setPixmap(dateSetting)

        # 初始化状态
        self.init_mode = "Steady aerobic"
        self.current_mode = self.init_mode
        self.init_mode_text = "Steady aerobic >"
        self.target_time_value = 1
        self.button_type_selection.setText(self.init_mode_text)
        self.button_time_setting.setText("1 minute >")
        self.button_trainging_date.setText(QDate.currentDate().toString("MMM d, yyyy >"))

        # 网络错误提示初始化（悬浮小标签，默认隐藏）
        self.network_error_tip = NetworkErrorTipLabel(self)
        self.network_error_tip.hide()

        # 用户ID
        self.user_id = UserSession.get_user_id()
        self.start_time = QDateTime.currentDateTime()
        self.end_time = QDateTime.currentDateTime()
        self.really_time = 0.0

        self.bind()

    def bind(self):
        # 绑定信号
        self.button_type_selection.clicked.connect(self.open_type_dialog)
        self.button_time_setting.clicked.connect(self.open_time_dialog)
        self.button_trainging_date.clicked.connect(self.open_date_dialog)
        self.button_complete.clicked.connect(self.complete_aerobic)
        self.button_start.clicked.connect(self.start_aerobic)

    def start_aerobic(self):
        """转至有氧运动运行界面"""
        if not self.validate_aerobic_name():
            return

        name = self.lineEdit_Aerobic_name.text()
        mode = self.current_mode
        target_time = self.target_time_value

        dialog = ImplementAerobicDialog(self, aerobic_name=name, aerobic_mode=mode, target_time=target_time)
        dialog.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)

        dialog.aerobic_finished.connect(self.handle_aerobic_finished)

        dialog.show()
        dialog.raise_()
        dialog.activateWindow()

    def handle_aerobic_finished(self, really_time, start_date):
        """处理有氧运动完成信号"""
        # 记录开始时间和结束时间
        self.start_time = start_date
        self.really_time = really_time

        # 调用发送请求函数
        self.complete_aerobic()

    def validate_aerobic_name(self):
        """验证有氧名称是否为空"""
        return self.lineEdit_Aerobic_name.text() != ""

    def open_type_dialog(self):
        """打开类型选择对话框"""
        self.mask = MaskWidget(self)
        self.mask.show()

        dialog = TypeSelectionDialog(self)
        parent_geometry = self.geometry()
        dialog_geometry = dialog.frameGeometry()
        center_point = parent_geometry.center()
        dialog_geometry.moveCenter(center_point)
        dialog.move(dialog_geometry.topLeft())

        dialog.type_confirmed.connect(self.update_type_display)
        dialog.exec()

        self.mask.close()

    def update_type_display(self, type_name, seconds):
        """更新类型显示"""
        self.current_mode = type_name
        if type_name == "Interval spead":
            self.button_type_selection.setText(f"Interval spead，{seconds }seconds >")
        else:
            self.button_type_selection.setText(f"{type_name} >")

    def open_time_dialog(self):
        """打开时间设置对话框"""
        self.mask = MaskWidget(self)
        self.mask.show()

        dialog = TimeSettingDialog(self)
        parent_geometry = self.geometry()
        dialog_geometry = dialog.frameGeometry()
        center_point = parent_geometry.center()
        dialog_geometry.moveCenter(center_point)
        dialog.move(dialog_geometry.topLeft())

        # 这里绑定信号到自定义槽函数
        dialog.time_confirmed.connect(self.on_time_confirmed)
        dialog.exec()

        self.mask.close()

    def on_time_confirmed(self, minutes):
        """接收时间选择对话框发来的时间，更新按钮显示和内部变量"""
        self.target_time_value = minutes  # 保存目标时间
        self.button_time_setting.setText(f"{minutes} minute>")

    def open_date_dialog(self):
        """打开日期设置对话框"""
        self.mask = MaskWidget(self)
        self.mask.show()

        dialog = DateDialog(self)
        parent_geometry = self.geometry()
        dialog_geometry = dialog.frameGeometry()
        center_point = parent_geometry.center()
        dialog_geometry.moveCenter(center_point)
        dialog.move(dialog_geometry.topLeft())
        dialog.date_confirmed.connect(lambda d: self.button_trainging_date.setText(d.toString("yyyy-MM-dd")))
        dialog.exec()

        self.mask.close()

    def calculate_aerobic_times(self):
        """计算有氧运动的实际时长、结束时间及格式化时间字符串"""
        if self.start_time is None or self.really_time is None:
            return None, None, "", ""

        # 直接用秒数计算结束时间
        self.end_time = self.start_time.addSecs(int(self.really_time))

        # 转成分钟用于显示和传输
        really_time_minutes = self.really_time / 60.0

        start_date_str = self.start_time.toString("yyyy-MM-dd HH:mm:ss")
        end_date_str = self.end_time.toString("yyyy-MM-dd HH:mm:ss")

        return really_time_minutes, self.end_time, start_date_str, end_date_str

    def complete_aerobic(self):
        """完成有氧，使用成员变量self.start_time和self.really_time计算"""
        if not self.validate_aerobic_name():
            self.show_tip("Please enter aerobic name.", success=False)
            return

        user_id = self.user_id
        name = self.lineEdit_Aerobic_name.text()
        type_ = "steady" if self.current_mode == self.init_mode else "interval"
        target_time = self.target_time_value

        really_time, end_time, start_date, end_date = self.calculate_aerobic_times()

        if really_time is None or start_date == "" or end_date == "":
            self.show_tip("Start time or duration not set.", success=False)
            return

        response = AerobicService.request_aerobic_complete(
            user_id,
            name,
            type_,
            really_time,
            target_time,
            start_date,
            end_date,
        )

        if response is None:
            self.show_tip("Network error, please try again!", success=False)
            return

        try:
            data = response.json()
        except ValueError:
            self.show_tip("Invalid server response.", success=False)
            return

        if response.status_code == 200:
            message = data.get("message", "Aerobic completed!")
            self.show_tip(message, success=True)
            print("Successfully!", message)
            self.close()  # 完成后关闭窗口
        else:
            message = data.get("detail", "Aerobic submission failed.")
            self.show_tip(message, success=False)
            print("Failed:", message)

    def show_tip(self, message, success=True):
        """用NetworkErrorTipLabel显示提示，自动处理消息类型和样式"""
        # 如果是列表或者字典，转成字符串显示，防止setText报错
        if not isinstance(message, str):
            if isinstance(message, list) or isinstance(message, dict):
                message = json.dumps(message, ensure_ascii=False, indent=2)
            else:
                message = str(message)

        if success:
            self.network_error_tip.setStyleSheet("color: white; background-color: rgba(0, 128, 0, 180);")
        else:
            self.network_error_tip.setStyleSheet("color: white; background-color: rgba(255, 0, 0, 180);")

        self.network_error_tip.show_message(message)

