# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FitMind_Client_MealRecord.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)
from ..res_rc import *

class Ui_Widget_MealRecord(object):
    def setupUi(self, Widget_MealRecord):
        if not Widget_MealRecord.objectName():
            Widget_MealRecord.setObjectName(u"Widget_MealRecord")
        Widget_MealRecord.resize(362, 700)
        Widget_MealRecord.setMinimumSize(QSize(300, 666))
        self.verticalLayout_2 = QVBoxLayout(Widget_MealRecord)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Widget_MealRecord)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame{\n"
"	border-top-right-radius:20px;\n"
"	border-top-left-radius:20px;\n"
"	border-bottom-right-radius:20px;\n"
"	border-bottom-left-radius:20px;\n"
"	background-color: white;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_head = QFrame(self.frame)
        self.frame_head.setObjectName(u"frame_head")
        self.frame_head.setStyleSheet(u"QFrame{\n"
"background-color:white;\n"
"	border-top-right-radius:20px;\n"
"	border-top-left-radius:20px;\n"
"	border-bottom-right-radius:20px;\n"
"	border-bottom-left-radius:20px;\n"
"}")
        self.frame_head.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_head.setFrameShadow(QFrame.Shadow.Raised)
        self.button_return = QPushButton(self.frame_head)
        self.button_return.setObjectName(u"button_return")
        self.button_return.setGeometry(QRect(10, 18, 28, 24))
        self.button_return.setStyleSheet(u"QPushButton{\n"
"background-color:transparent;\n"
"border-radius:10px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icon/back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_return.setIcon(icon)
        self.button_return.setIconSize(QSize(24, 24))
        self.label = QLabel(self.frame_head)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 20, 105, 21))
        self.label.setStyleSheet(u"font: 700 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.verticalLayout.addWidget(self.frame_head)

        self.frame_center = QFrame(self.frame)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setStyleSheet(u"QFrame{\n"
"background-color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"	font:14px \"\u5fae\u8f6f\u96c5\u9ed1\"\n"
"}")
        self.frame_center.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_center.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_center)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_foodname = QLineEdit(self.frame_center)
        self.lineEdit_foodname.setObjectName(u"lineEdit_foodname")
        self.lineEdit_foodname.setMinimumSize(QSize(0, 40))
        self.lineEdit_foodname.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(225, 225, 225);\n"
"border-radius:10px;\n"
"margin-left:10px;\n"
"margin-right:10px;\n"
"}")

        self.verticalLayout_3.addWidget(self.lineEdit_foodname)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_search = QPushButton(self.frame_center)
        self.button_search.setObjectName(u"button_search")
        self.button_search.setMinimumSize(QSize(75, 45))
        self.button_search.setMaximumSize(QSize(100, 16777215))
        self.button_search.setStyleSheet(u"QPushButton{\n"
"background-color:white;\n"
"border: none;          /* \u79fb\u9664\u8fb9\u6846 */\n"
"outline: none; \n"
"}")

        self.horizontalLayout.addWidget(self.button_search)

        self.button_customize = QPushButton(self.frame_center)
        self.button_customize.setObjectName(u"button_customize")
        self.button_customize.setMinimumSize(QSize(75, 45))
        self.button_customize.setMaximumSize(QSize(100, 16777215))
        self.button_customize.setStyleSheet(u"QPushButton{\n"
"background-color:white;\n"
"border: none;          /* \u79fb\u9664\u8fb9\u6846 */\n"
"outline: none; \n"
"}")

        self.horizontalLayout.addWidget(self.button_customize)

        self.button_collect = QPushButton(self.frame_center)
        self.button_collect.setObjectName(u"button_collect")
        self.button_collect.setMinimumSize(QSize(75, 45))
        self.button_collect.setMaximumSize(QSize(100, 16777215))
        self.button_collect.setStyleSheet(u"QPushButton{\n"
"background-color:white;\n"
"border: none;          /* \u79fb\u9664\u8fb9\u6846 */\n"
"}")

        self.horizontalLayout.addWidget(self.button_collect)

        self.button_set = QPushButton(self.frame_center)
        self.button_set.setObjectName(u"button_set")
        self.button_set.setMinimumSize(QSize(75, 45))
        self.button_set.setMaximumSize(QSize(100, 16777215))
        self.button_set.setStyleSheet(u"QPushButton{\n"
"background-color:white;\n"
"border: none;          /* \u79fb\u9664\u8fb9\u6846 */\n"
"outline: none; \n"
"}")

        self.horizontalLayout.addWidget(self.button_set)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.stackedWidget = QStackedWidget(self.frame_center)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_search = QWidget()
        self.page_search.setObjectName(u"page_search")
        self.verticalLayout_4 = QVBoxLayout(self.page_search)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page_search)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
"	border:none\n"
"}\n"
"\n"
"QWidget {\n"
"    background: transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 4px;\n"
"    margin: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgba(100, 100, 100, 0.5);\n"
"    min-height: 20px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgba(100, 100, 100, 0.8);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 4px;\n"
"    margin: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgba(100, 100, 100, 0.5);\n"
"    min-width: 20px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rg"
                        "ba(100, 100, 100, 0.8);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 360, 477))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_search)
        self.page_collect = QWidget()
        self.page_collect.setObjectName(u"page_collect")
        self.stackedWidget.addWidget(self.page_collect)
        self.page_set = QWidget()
        self.page_set.setObjectName(u"page_set")
        self.stackedWidget.addWidget(self.page_set)
        self.page_customize = QWidget()
        self.page_customize.setObjectName(u"page_customize")
        self.stackedWidget.addWidget(self.page_customize)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 9)

        self.verticalLayout.addWidget(self.frame_center)

        self.frame_foot = QFrame(self.frame)
        self.frame_foot.setObjectName(u"frame_foot")
        self.frame_foot.setStyleSheet(u"QFrame{\n"
"background-color:white;\n"
"	border-top-right-radius:20px;\n"
"	border-top-left-radius:20px;\n"
"	border-bottom-right-radius:20px;\n"
"	border-bottom-left-radius:20px;\n"
"}")
        self.frame_foot.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_foot.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_foot)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_list = QToolButton(self.frame_foot)
        self.button_list.setObjectName(u"button_list")
        self.button_list.setStyleSheet(u"#button_list{\n"
"	background-color: transparent;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/\u98df\u7269\u7ba1\u7406.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_list.setIcon(icon1)
        self.button_list.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.button_list)

        self.button_confrim = QPushButton(self.frame_foot)
        self.button_confrim.setObjectName(u"button_confrim")
        self.button_confrim.setMinimumSize(QSize(0, 41))
        self.button_confrim.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(51, 10, 255);\n"
"color:white;\n"
"	font: 700 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"border-radius:15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.button_confrim)


        self.verticalLayout.addWidget(self.frame_foot)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 9)
        self.verticalLayout.setStretch(2, 1)

        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Widget_MealRecord)
        self.button_return.clicked.connect(Widget_MealRecord.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget_MealRecord)
    # setupUi

    def retranslateUi(self, Widget_MealRecord):
        Widget_MealRecord.setWindowTitle(QCoreApplication.translate("Widget_MealRecord", u"Form", None))
        self.button_return.setText("")
        self.label.setText(QCoreApplication.translate("Widget_MealRecord", u"Record lunch", None))
        self.lineEdit_foodname.setPlaceholderText(QCoreApplication.translate("Widget_MealRecord", u"Enter the name  of the  food", None))
        self.button_search.setText(QCoreApplication.translate("Widget_MealRecord", u"Search", None))
        self.button_customize.setText(QCoreApplication.translate("Widget_MealRecord", u"Customize", None))
        self.button_collect.setText(QCoreApplication.translate("Widget_MealRecord", u"Collect", None))
        self.button_set.setText(QCoreApplication.translate("Widget_MealRecord", u"Set", None))
        self.button_list.setText("")
        self.button_confrim.setText(QCoreApplication.translate("Widget_MealRecord", u"CONFIRM", None))
    # retranslateUi

