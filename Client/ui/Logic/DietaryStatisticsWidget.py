# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QLocale, QMetaObject, Qt)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDialog,
                               QPushButton, QVBoxLayout, QWidget)

from Client.ui.Designer.ui_DietaryStatistics import Ui_Widget_DietaryStatistics


class CalendarDialog(QWidget):
    def __init__(self, initial_date=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Date")
        self.calendar = QCalendarWidget(self)
        self.calendar.setLocale(QLocale(QLocale.English))  # 设置英文显示
        if initial_date:
            self.calendar.setSelectedDate(initial_date)
        layout = QVBoxLayout(self)
        layout.addWidget(self.calendar)
        self.calendar.clicked.connect(self.accept)

    def selectedDate(self):
        return self.calendar.selectedDate()


class DietaryStatisticsWidget(QWidget, Ui_Widget_DietaryStatistics):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 初始化日期为当前日期
        self.start_date = QDate.currentDate()
        self.end_date = QDate.currentDate()

        # 设置初始按钮文本
        self.update_date_buttons()

        # 连接信号槽
        self.button_startDate.clicked.connect(self.on_start_date_clicked)
        self.button_endDate.clicked.connect(self.on_end_date_clicked)

    def get_ordinal_suffix(self, day):
        """获取日期的序数后缀"""
        if 11 <= (day % 100) <= 13:
            return 'th'
        return {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')

    def update_date_buttons(self):
        """更新日期按钮的显示"""
        english_locale = QLocale(QLocale.English)

        # 处理开始日期
        start_month = english_locale.toString(self.start_date, "MMMM")
        start_day = self.start_date.day()
        start_str = f"{start_month} {start_day}{self.get_ordinal_suffix(start_day)}"
        self.button_startDate.setText(start_str)

        # 处理结束日期
        end_month = english_locale.toString(self.end_date, "MMMM")
        end_day = self.end_date.day()
        end_str = f"{end_month} {end_day}{self.get_ordinal_suffix(end_day)}"
        self.button_endDate.setText(end_str)

    def on_start_date_clicked(self):
        """处理开始日期点击事件"""
        dialog = CalendarDialog(self.start_date, self)
        if dialog.exec() == QDialog.Accepted:
            self.start_date = dialog.selectedDate()
            if self.start_date > self.end_date:
                self.end_date = self.start_date  # 自动调整结束日期
            self.update_date_buttons()

    def on_end_date_clicked(self):
        """处理结束日期点击事件"""
        dialog = CalendarDialog(self.end_date, self)
        if dialog.exec() == QDialog.Accepted:
            new_date = dialog.selectedDate()
            if new_date >= self.start_date:
                self.end_date = new_date
                self.update_date_buttons()

