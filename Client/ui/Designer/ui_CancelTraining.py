# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FitMind_Client_CancelTraining.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
from ..res_rc import *

class Ui_Dialog_cancel_training(object):
    def setupUi(self, Dialog_cancel_training):
        if not Dialog_cancel_training.objectName():
            Dialog_cancel_training.setObjectName(u"Dialog_cancel_training")
        Dialog_cancel_training.resize(377, 276)
        self.horizontalLayout = QHBoxLayout(Dialog_cancel_training)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Dialog_cancel_training)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-top-right-radius:40px;\n"
"	border-top-left-radius:40px;\n"
"	border-bottom-right-radius:40px;\n"
"	border-bottom-left-radius:40px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\"; \n"
"    border: 1px solid #ccc; /* \u7ec6\u8fb9\u6846 */\n"
"    border-radius: 16px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: white; /* \u7eaf\u767d\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"	border:none;\n"
"    min-width: 60px;\n"
"    min-height: 35px;\n"
"	margin:0 65px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f0f0f0; /* \u6d45\u7070\u8272\u60ac\u6d6e\u6548\u679c */\n"
"    padding-bottom: 2px; /* \u8f7b\u5fae\u4e0b\u79fb\uff0c\u589e\u52a0\u6309\u538b\u611f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0; /* \u66f4\u6df1\u7684\u7070\u8272\uff0c\u6309\u4e0b\u6548\u679c */\n"
"    padding-bottom: 1px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    b"
                        "ackground-color: #f8f8f8;\n"
"    color: gray;\n"
"    border-color: #ddd;\n"
"}\n"
"\n"
"#button_cancel_training{\n"
"	background-color: #ff0000;\n"
"	    color: white; \n"
"}\n"
"\n"
"#button_cancel_training:hover {\n"
"    background-color: #ff0000;\n"
"}\n"
"\n"
"#button_cancel_training:pressed {\n"
"    background-color:#ffe1e0; \n"
"}\n"
"\n"
"#button_cancel{\n"
"	margin-bottom:20px;\n"
"}\n"
"\n"
"#button_cancel:pressed {\n"
"	color:white;\n"
"}\n"
"\n"
"#label_2{\n"
"	\n"
"	font: 700 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"\n"
"#label{\n"
"	font:10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_cancel_icon = QLabel(self.frame)
        self.label_cancel_icon.setObjectName(u"label_cancel_icon")

        self.verticalLayout.addWidget(self.label_cancel_icon)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.button_cancel_training = QPushButton(self.frame)
        self.button_cancel_training.setObjectName(u"button_cancel_training")

        self.verticalLayout.addWidget(self.button_cancel_training)

        self.button_cancel = QPushButton(self.frame)
        self.button_cancel.setObjectName(u"button_cancel")

        self.verticalLayout.addWidget(self.button_cancel)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog_cancel_training)

        QMetaObject.connectSlotsByName(Dialog_cancel_training)
    # setupUi

    def retranslateUi(self, Dialog_cancel_training):
        Dialog_cancel_training.setWindowTitle(QCoreApplication.translate("Dialog_cancel_training", u"Dialog", None))
        self.label_cancel_icon.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog_cancel_training", u"Cancel Training", None))
        self.label.setText(QCoreApplication.translate("Dialog_cancel_training", u"You haven't added any actions yet", None))
        self.button_cancel_training.setText(QCoreApplication.translate("Dialog_cancel_training", u"Cancel this training", None))
        self.button_cancel.setText(QCoreApplication.translate("Dialog_cancel_training", u"return", None))
    # retranslateUi

