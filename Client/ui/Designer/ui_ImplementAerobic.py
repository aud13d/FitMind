# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FitMind_Client_ImplementAerobic.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_ImplementAerobicDialog(object):
    def setupUi(self, ImplementAerobicDialog):
        if not ImplementAerobicDialog.objectName():
            ImplementAerobicDialog.setObjectName(u"ImplementAerobicDialog")
        ImplementAerobicDialog.resize(362, 700)
        ImplementAerobicDialog.setMinimumSize(QSize(300, 666))
        self.verticalLayout_2 = QVBoxLayout(ImplementAerobicDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(ImplementAerobicDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame{\n"
"	background-color:rgb(0, 0, 89);\n"
"	border-top-right-radius:20px;\n"
"	border-top-left-radius:20px;\n"
"	border-bottom-right-radius:20px;\n"
"	border-bottom-left-radius:20px;\n"
"}\n"
"\n"
"\n"
"#button_back {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 6px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: white; /* \u7eaf\u767d\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"    min-width: 60px;\n"
"    min-height: 45px;\n"
"\n"
"}\n"
"\n"
"#button_back:hover {\n"
"    background-color: #f0f0f0; /* \u6d45\u7070\u8272\u60ac\u6d6e\u6548\u679c */\n"
"    margin-top: 2px; /* \u8f7b\u5fae\u4e0b\u79fb\uff0c\u589e\u52a0\u6309\u538b\u611f */\n"
"}\n"
"\n"
"#button_back:pressed {\n"
"    background-color: #e0e0e0; /* \u6309\u4e0b\u65f6\u53d8\u6df1\u7070 */\n"
"    margin-top: 1px; /* \u6309\u4e0b\u65f6\u8f7b\u5fae\u4e0a\u79fb */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #f8f8f8;\n"
"    color: gray;\n"
"    border-color: #dd"
                        "d;\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"	font: 700 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color: white\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_aerobic_state = QLabel(self.frame)
        self.label_aerobic_state.setObjectName(u"label_aerobic_state")
        self.label_aerobic_state.setGeometry(QRect(10, 40, 211, 16))
        self.label_aerobic_state.setStyleSheet(u"color:rgb(85, 85, 127)")
        self.label_aerobic_name = QLabel(self.frame)
        self.label_aerobic_name.setObjectName(u"label_aerobic_name")
        self.label_aerobic_name.setGeometry(QRect(10, 10, 111, 21))
        self.label_aerobic_name.setStyleSheet(u"color:white")
        self.label_aerobic_time = QLabel(self.frame)
        self.label_aerobic_time.setObjectName(u"label_aerobic_time")
        self.label_aerobic_time.setGeometry(QRect(60, 200, 221, 151))
        self.label_aerobic_time.setStyleSheet(u"font: 700 56pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color:rgb(255, 255, 255)")
        self.label_aerobic_hint = QLabel(self.frame)
        self.label_aerobic_hint.setObjectName(u"label_aerobic_hint")
        self.label_aerobic_hint.setGeometry(QRect(0, 330, 341, 20))
        self.label_aerobic_hint.setStyleSheet(u"font:Regular 24px ;\n"
"color:rgb(198, 198, 198);")
        self.label_aerobic_hint.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_aerboic_start = QPushButton(self.frame)
        self.button_aerboic_start.setObjectName(u"button_aerboic_start")
        self.button_aerboic_start.setGeometry(QRect(120, 470, 100, 100))
        self.button_aerboic_start.setStyleSheet(u"            QPushButton {\n"
"                background-color: rgb(30, 205, 30);  /* \u7eff\u8272\u80cc\u666f */\n"
"                color: white;               /* \u9ed1\u8272\u5b57\u4f53 */\n"
"				font: 700 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"                border: none;\n"
"                border-radius: 50px;       /* \u534a\u5f84 = \u5bbd\u9ad8\u4e00\u534a\uff0c\u5f62\u6210\u5706\u5f62 */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #45a049;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #388E3C;\n"
"            }")
        self.button_aerobic_quit = QPushButton(self.frame)
        self.button_aerobic_quit.setObjectName(u"button_aerobic_quit")
        self.button_aerobic_quit.setGeometry(QRect(280, 10, 30, 21))
        self.button_aerobic_quit.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	color:white;\n"
"	font: 700 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}")

        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(ImplementAerobicDialog)
        self.button_aerobic_quit.clicked.connect(ImplementAerobicDialog.close)

        QMetaObject.connectSlotsByName(ImplementAerobicDialog)
    # setupUi

    def retranslateUi(self, ImplementAerobicDialog):
        ImplementAerobicDialog.setWindowTitle(QCoreApplication.translate("ImplementAerobicDialog", u"Dialog", None))
        self.label_aerobic_state.setText(QCoreApplication.translate("ImplementAerobicDialog", u"Not started", None))
        self.label_aerobic_name.setText(QCoreApplication.translate("ImplementAerobicDialog", u"aerobic_name", None))
        self.label_aerobic_time.setText(QCoreApplication.translate("ImplementAerobicDialog", u"00:00", None))
        self.label_aerobic_hint.setText(QCoreApplication.translate("ImplementAerobicDialog", u"hint", None))
        self.button_aerboic_start.setText(QCoreApplication.translate("ImplementAerobicDialog", u"Start", None))
        self.button_aerobic_quit.setText(QCoreApplication.translate("ImplementAerobicDialog", u"Exit", None))
    # retranslateUi

