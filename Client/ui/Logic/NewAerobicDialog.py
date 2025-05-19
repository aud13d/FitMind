from PySide6 import QtCore
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QDialog
)

from Client.config import TypeSelectionNewAerobicDialog_IconPath, TimeSettingNewAerobicDialog_IconPath
from Client.ui.Components.MaskWidget import MaskWidget
from Client.ui.Designer.ui_NewAerobic import Ui_NewAerobicDialog
from Client.ui.Components.TypeSelectionDialog import TypeSelectionDialog
from Client.ui.Components.DateDialog import DateDialog
from Client.ui.Components.TimeSettingDialog import TimeSettingDialog

class NewAerobicDialog(QDialog, Ui_NewAerobicDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        if parent:
            self.setGeometry(parent.geometry())

        icon_pixmap_typeSelection = QPixmap(TypeSelectionNewAerobicDialog_IconPath)
        typeSelection = icon_pixmap_typeSelection.scaled(16, 16, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.icon_type_selection.setPixmap(typeSelection)

        icon_pixmap_dateSetting = QPixmap(TimeSettingNewAerobicDialog_IconPath)
        dateSetting = icon_pixmap_dateSetting.scaled(16, 16, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.icon_time_setting.setPixmap(dateSetting)
        self.icon_training_date.setPixmap(dateSetting)

        # 初始化状态
        self.current_mode = "Uniform Aerobic"
        self.button_time_setting.setText(QDate.currentDate().toString("MMM d, yyyy"))

        self.bind()

    def bind(self):
        # 绑定信号
        self.button_type_selection.clicked.connect(self.open_type_dialog)
        self.button_time_setting.clicked.connect(self.open_time_dialog)
        self.button_trainging_date.clicked.connect(self.open_date_dialog)

    def open_type_dialog(self):
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
        self.current_mode = type_name
        if type_name == "Variable Speed Aerobic":
            self.button_type_selection.setText(f"Variable Speed，{seconds }seconds >")
        else:
            self.button_type_selection.setText(f"{type_name} >")

    def open_time_dialog(self):
        self.mask = MaskWidget(self)
        self.mask.show()

        dialog = TimeSettingDialog(self)
        parent_geometry = self.geometry()
        dialog_geometry = dialog.frameGeometry()
        center_point = parent_geometry.center()
        dialog_geometry.moveCenter(center_point)
        dialog.move(dialog_geometry.topLeft())

        dialog.time_confirmed.connect(lambda m: self.button_time_setting.setText(f"{m} minute>"))
        dialog.exec()

        self.mask.close()

    def open_date_dialog(self):
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

