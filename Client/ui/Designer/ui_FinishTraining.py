# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FitMind_Client_FinishTraining.ui'
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

class Ui_Dialog_finish_training(object):
    def setupUi(self, Dialog_finish_training):
        if not Dialog_finish_training.objectName():
            Dialog_finish_training.setObjectName(u"Dialog_finish_training")
        Dialog_finish_training.resize(378, 278)
        self.horizontalLayout = QHBoxLayout(Dialog_finish_training)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Dialog_finish_training)
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
"#button_generate_sharing{\n"
"	background-color: #5555ff;\n"
"	    color: white; \n"
"}\n"
"\n"
"#button_generate_sharing:hover {\n"
"    background-color:#5555ff;\n"
"}\n"
"\n"
"#button_generate_sharing:pressed {\n"
"    background-color: #c9feff; \n"
"}\n"
"\n"
"\n"
"\n"
"#button_cancel:pressed {\n"
"	color:white;\n"
"	\n"
"}\n"
"\n"
"\n"
"#button_finish:pressed {\n"
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
        self.label_finish_icon = QLabel(self.frame)
        self.label_finish_icon.setObjectName(u"label_finish_icon")

        self.verticalLayout.addWidget(self.label_finish_icon)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.button_generate_sharing = QPushButton(self.frame)
        self.button_generate_sharing.setObjectName(u"button_generate_sharing")

        self.verticalLayout.addWidget(self.button_generate_sharing)

        self.button_finish = QPushButton(self.frame)
        self.button_finish.setObjectName(u"button_finish")

        self.verticalLayout.addWidget(self.button_finish)

        self.button_cancel = QPushButton(self.frame)
        self.button_cancel.setObjectName(u"button_cancel")

        self.verticalLayout.addWidget(self.button_cancel)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog_finish_training)
        self.button_cancel.clicked.connect(Dialog_finish_training.close)

        QMetaObject.connectSlotsByName(Dialog_finish_training)
    # setupUi

    def retranslateUi(self, Dialog_finish_training):
        Dialog_finish_training.setWindowTitle(QCoreApplication.translate("Dialog_finish_training", u"Dialog", None))
        self.label_finish_icon.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog_finish_training", u"Finish Training", None))
        self.label.setText(QCoreApplication.translate("Dialog_finish_training", u"Have you completed the training?", None))
        self.button_generate_sharing.setText(QCoreApplication.translate("Dialog_finish_training", u"Finish and generate a sharing image", None))
        self.button_finish.setText(QCoreApplication.translate("Dialog_finish_training", u"finish", None))
        self.button_cancel.setText(QCoreApplication.translate("Dialog_finish_training", u"return", None))
    # retranslateUi

