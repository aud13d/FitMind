# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FitMind_Client_BodyData.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

from Client.ui.Components.ClickableLabel import ClickableLabel
from ..res_rc import *

class Ui_Widget_BodyData(object):
    def setupUi(self, Widget_BodyData):
        if not Widget_BodyData.objectName():
            Widget_BodyData.setObjectName(u"Widget_BodyData")
        Widget_BodyData.resize(362, 700)
        Widget_BodyData.setMinimumSize(QSize(300, 666))
        self.verticalLayout = QVBoxLayout(Widget_BodyData)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Widget_BodyData)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-bottom-right-radius:20px;\n"
"	border-bottom-left-radius:20px;\n"
"	border-top-right-radius:20px;\n"
"	border-top-left-radius:20px;\n"
"	border:none\n"
"}\n"
"\n"
"QPushButton {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 6px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: white; /* \u7eaf\u767d\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"    min-width: 60px;\n"
"    min-height: 25px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f0f0f0; /* \u6d45\u7070\u8272\u60ac\u6d6e\u6548\u679c */\n"
"    margin-top: 2px; /* \u8f7b\u5fae\u4e0b\u79fb\uff0c\u589e\u52a0\u6309\u538b\u611f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0; /* \u6309\u4e0b\u65f6\u53d8\u6df1\u7070 */\n"
"    margin-top: 1px; /* \u6309\u4e0b\u65f6\u8f7b\u5fae\u4e0a\u79fb */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #f8f8f8;\n"
"    color: gray;\n"
"    b"
                        "order-color: #ddd;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 6, 0, 6)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, -1, 6, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, -1, 6, -1)
        self.button_body_back = QPushButton(self.frame)
        self.button_body_back.setObjectName(u"button_body_back")
        self.button_body_back.setStyleSheet(u"padding-left: -16px;")
        icon = QIcon()
        icon.addFile(u":/icons/icon/back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_body_back.setIcon(icon)
        self.button_body_back.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.button_body_back)

        self.horizontalSpacer = QSpacerItem(218, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QPushButton {\n"
"    	background-color: #dedede;\n"
"    border: 0 solid transparent;  /* \u900f\u660e\u8fb9\u6846 */\n"
"    border-radius: 6px;\n"
"font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	    min-width: 30px;\n"
"    min-height: 15px;\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color :#dedede;\n"
"	border-radius:6px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: white;  \n"
"	font: 700 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(6, 4, 6, 4)
        self.button_body_kg = QPushButton(self.frame_4)
        self.button_body_kg.setObjectName(u"button_body_kg")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_body_kg.sizePolicy().hasHeightForWidth())
        self.button_body_kg.setSizePolicy(sizePolicy)
        self.button_body_kg.setMinimumSize(QSize(30, 15))
        self.button_body_kg.setStyleSheet(u"")
        self.button_body_kg.setCheckable(True)
        self.button_body_kg.setChecked(True)

        self.horizontalLayout_5.addWidget(self.button_body_kg)

        self.button_body_g = QPushButton(self.frame_4)
        self.button_body_g.setObjectName(u"button_body_g")
        sizePolicy.setHeightForWidth(self.button_body_g.sizePolicy().hasHeightForWidth())
        self.button_body_g.setSizePolicy(sizePolicy)
        self.button_body_g.setMinimumSize(QSize(30, 15))
        self.button_body_g.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.button_body_g)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton {\n"
"    border: 0 solid transparent;  /* \u900f\u660e\u8fb9\u6846 */\n"
"    border-radius: 6px;\n"
"font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	background-color: #dedede;\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color :#dedede;\n"
"	border-radius:6px;\n"
"    margin-left: 6px;\n"
"    margin-right: 6px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: white;  \n"
"	font: 700 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 4, 6, 4)
        self.button_body_data = QPushButton(self.frame_3)
        self.button_body_data.setObjectName(u"button_body_data")
        sizePolicy.setHeightForWidth(self.button_body_data.sizePolicy().hasHeightForWidth())
        self.button_body_data.setSizePolicy(sizePolicy)
        self.button_body_data.setCheckable(True)
        self.button_body_data.setChecked(True)

        self.horizontalLayout_3.addWidget(self.button_body_data)

        self.button_body_graph = QPushButton(self.frame_3)
        self.button_body_graph.setObjectName(u"button_body_graph")
        sizePolicy.setHeightForWidth(self.button_body_graph.sizePolicy().hasHeightForWidth())
        self.button_body_graph.setSizePolicy(sizePolicy)
        self.button_body_graph.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.button_body_graph)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, -1, 6, -1)
        self.label_body_current_weight = ClickableLabel(self.frame)
        self.label_body_current_weight.setObjectName(u"label_body_current_weight")
        self.label_body_current_weight.setStyleSheet(u"#label_body_current_weight {\n"
"    background-color: #dedede;\n"
"    width: 100px;\n"
"    height: 40x;\n"
"    border-radius: 6px;      /* \u5706\u89d2 */\n"
"    text-align: left;       /* \u6587\u5b57\u9760\u5de6 */\n"
"    padding-left: 8px;      /* \u52a0\u70b9\u5185\u8fb9\u8ddd\u8ba9\u6587\u5b57\u4e0d\u8d34\u8fb9 */\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_body_current_weight)

        self.label_body_target_weight = ClickableLabel(self.frame)
        self.label_body_target_weight.setObjectName(u"label_body_target_weight")
        self.label_body_target_weight.setStyleSheet(u"#label_body_target_weight {\n"
"    background-color: #dedede;\n"
"    width: 100px;\n"
"    height: 40x;\n"
"    border-radius: 6px;      /* \u5706\u89d2 */\n"
"    text-align: left;       /* \u6587\u5b57\u9760\u5de6 */\n"
"    padding-left: 8px;      /* \u52a0\u70b9\u5185\u8fb9\u8ddd\u8ba9\u6587\u5b57\u4e0d\u8d34\u8fb9 */\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_body_target_weight)

        self.label_body_body_fat = ClickableLabel(self.frame)
        self.label_body_body_fat.setObjectName(u"label_body_body_fat")
        self.label_body_body_fat.setStyleSheet(u"#label_body_body_fat {\n"
"    background-color: #dedede;\n"
"    width: 100px;\n"
"    height: 40px;\n"
"    border-radius: 6px;      /* \u5706\u89d2 */\n"
"    text-align: left;       /* \u6587\u5b57\u9760\u5de6 */\n"
"    padding-left: 8px;      /* \u52a0\u70b9\u5185\u8fb9\u8ddd\u8ba9\u6587\u5b57\u4e0d\u8d34\u8fb9 */\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_body_body_fat)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 9)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_body_data = QWidget()
        self.page_body_data.setObjectName(u"page_body_data")
        self.stackedWidget.addWidget(self.page_body_data)
        self.page_body_graph = QWidget()
        self.page_body_graph.setObjectName(u"page_body_graph")
        self.stackedWidget.addWidget(self.page_body_graph)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 3)

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Widget_BodyData)
        self.button_body_back.clicked.connect(Widget_BodyData.close)

        QMetaObject.connectSlotsByName(Widget_BodyData)
    # setupUi

    def retranslateUi(self, Widget_BodyData):
        Widget_BodyData.setWindowTitle(QCoreApplication.translate("Widget_BodyData", u"Form", None))
        self.button_body_back.setText("")
        self.button_body_kg.setText(QCoreApplication.translate("Widget_BodyData", u"Kg", None))
        self.button_body_g.setText(QCoreApplication.translate("Widget_BodyData", u"G", None))
        self.button_body_data.setText(QCoreApplication.translate("Widget_BodyData", u"data", None))
        self.button_body_graph.setText(QCoreApplication.translate("Widget_BodyData", u"graph", None))
        self.label_body_current_weight.setText(QCoreApplication.translate("Widget_BodyData", u"Current weight,\n"
"Date,\n"
"\n"
"Data kg", None))
        self.label_body_target_weight.setText(QCoreApplication.translate("Widget_BodyData", u"Target weight,\n"
"Date,\n"
"\n"
"Data kg", None))
        self.label_body_body_fat.setText(QCoreApplication.translate("Widget_BodyData", u"Body fat,\n"
"date,\n"
"\n"
"Data %", None))
    # retranslateUi

