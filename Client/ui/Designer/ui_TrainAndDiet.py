# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FitMind_Client_TrainAndDiet.ui'
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
    QLabel, QPushButton, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)
from ..res_rc import *

class Ui_Dialog_TD(object):
    def setupUi(self, Dialog_TD):
        if not Dialog_TD.objectName():
            Dialog_TD.setObjectName(u"Dialog_TD")
        Dialog_TD.resize(362, 500)
        Dialog_TD.setMinimumSize(QSize(300, 500))
        self.verticalLayout = QVBoxLayout(Dialog_TD)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog_TD)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet(u"font: 700 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.label_2)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet(u"#frame_6{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-top-right-radius:40px;\n"
"	border-top-left-radius:40px;\n"
"	border-bottom-right-radius:40px;\n"
"	border-bottom-left-radius:40px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 0, 6, 6)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 45))
        self.label.setMaximumSize(QSize(16777215, 45))
        self.label.setStyleSheet(u"font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label.setMargin(8)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 10, 6, 10)
        self.label_protein = QLabel(self.frame_6)
        self.label_protein.setObjectName(u"label_protein")
        self.label_protein.setMinimumSize(QSize(60, 80))
        self.label_protein.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_protein.setStyleSheet(u"QLabel {\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 9px; /* \u5706\u89d2 */\n"
"    background-color: lightyellow; /* \u80cc\u666f\u989c\u8272 */\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"    padding: 5px; /* \u5185\u8fb9\u8ddd */\n"
"}\n"
"")
        self.label_protein.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_protein)

        self.label_carbohydrate = QLabel(self.frame_6)
        self.label_carbohydrate.setObjectName(u"label_carbohydrate")
        self.label_carbohydrate.setMinimumSize(QSize(60, 80))
        self.label_carbohydrate.setStyleSheet(u"QLabel {\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 9px; /* \u5706\u89d2 */\n"
"    background-color: lightgreen; /* \u80cc\u666f\u989c\u8272 */\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"    padding: 5px; /* \u5185\u8fb9\u8ddd */\n"
"}\n"
"")
        self.label_carbohydrate.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_carbohydrate)

        self.label_fat = QLabel(self.frame_6)
        self.label_fat.setObjectName(u"label_fat")
        self.label_fat.setMinimumSize(QSize(60, 80))
        self.label_fat.setStyleSheet(u"QLabel {\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 9px; /* \u5706\u89d2 */\n"
"\n"
"	\n"
"	background-color: rgb(255, 144, 155);\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"    padding: 5px; /* \u5185\u8fb9\u8ddd */\n"
"}\n"
"")
        self.label_fat.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_fat)

        self.label_water = QLabel(self.frame_6)
        self.label_water.setObjectName(u"label_water")
        self.label_water.setMinimumSize(QSize(60, 80))
        self.label_water.setStyleSheet(u"QLabel {\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 9px; /* \u5706\u89d2 */\n"
"    background-color: lightblue; /* \u80cc\u666f\u989c\u8272 */\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"    padding: 5px; /* \u5185\u8fb9\u8ddd */\n"
"}\n"
"")
        self.label_water.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_water)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(3)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setStyleSheet(u"QToolButton {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	    border-radius: 15px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: white; /* \u7eaf\u767d\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"    min-width: 45px;\n"
"    min-height: 45px;\n"
"\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #f0f0f0; /* \u6d45\u7070\u8272\u60ac\u6d6e\u6548\u679c */\n"
"    margin-top: 2px; /* \u8f7b\u5fae\u4e0b\u79fb\uff0c\u589e\u52a0\u6309\u538b\u611f */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #e0e0e0; /* \u6309\u4e0b\u65f6\u53d8\u6df1\u7070 */\n"
"    margin-top: 1px; /* \u6309\u4e0b\u65f6\u8f7b\u5fae\u4e0a\u79fb */\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 9, -1, 9)
        self.button_new_train = QToolButton(self.frame_2)
        self.button_new_train.setObjectName(u"button_new_train")
        self.button_new_train.setStyleSheet(u"background-color: rgb(15, 255, 227);")
        icon = QIcon()
        icon.addFile(u":/icons/icon/yaling.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_new_train.setIcon(icon)
        self.button_new_train.setIconSize(QSize(32, 32))
        self.button_new_train.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self.horizontalLayout.addWidget(self.button_new_train)

        self.button_new_aerobic = QToolButton(self.frame_2)
        self.button_new_aerobic.setObjectName(u"button_new_aerobic")
        self.button_new_aerobic.setStyleSheet(u"background-color: rgb(135, 255, 165);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/paobuji.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_new_aerobic.setIcon(icon1)
        self.button_new_aerobic.setIconSize(QSize(32, 32))
        self.button_new_aerobic.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self.horizontalLayout.addWidget(self.button_new_aerobic)

        self.button_new_rest = QToolButton(self.frame_2)
        self.button_new_rest.setObjectName(u"button_new_rest")
        self.button_new_rest.setStyleSheet(u"background-color: rgb(255, 170, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/xiuxi.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_new_rest.setIcon(icon2)
        self.button_new_rest.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.button_new_rest)

        self.button_body_data = QToolButton(self.frame_2)
        self.button_body_data.setObjectName(u"button_body_data")
        self.button_body_data.setStyleSheet(u"background-color: rgb(255, 158, 171);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/stzx_renti.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_body_data.setIcon(icon3)
        self.button_body_data.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.button_body_data)

        self.button_menstrual_record = QToolButton(self.frame_2)
        self.button_menstrual_record.setObjectName(u"button_menstrual_record")
        self.button_menstrual_record.setStyleSheet(u"background-color: rgb(255, 11, 182);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/jingqi.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_menstrual_record.setIcon(icon4)
        self.button_menstrual_record.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.button_menstrual_record)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setStyleSheet(u"QPushButton {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	border: 1px solid #ccc; /* \u8bbe\u7f6e\u8fb9\u6846 */\n"
"    border-radius: 10px; /* \u8bbe\u7f6e\u5706\u89d2 */\n"
"    background-color: white; /* \u7eaf\u767d\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
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
"    background-color: #f8f8f8;\n"
"    color: gray;\n"
"    border-color: #ddd;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 40, 40, 23))
        self.pushButton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icon/delete-1--remove-add-button-buttons-delete-cross-x.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog_TD)
        self.pushButton.clicked.connect(Dialog_TD.close)

        QMetaObject.connectSlotsByName(Dialog_TD)
    # setupUi

    def retranslateUi(self, Dialog_TD):
        Dialog_TD.setWindowTitle(QCoreApplication.translate("Dialog_TD", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_TD", u" Diet Record", None))
        self.label.setText(QCoreApplication.translate("Dialog_TD", u"Already eaten 0/-- maximum calories", None))
        self.label_protein.setText(QCoreApplication.translate("Dialog_TD", u"Pro(g)\n"
"0\n"
"0% ", None))
        self.label_carbohydrate.setText(QCoreApplication.translate("Dialog_TD", u"Carbs(g)\n"
"0\n"
"0% ", None))
        self.label_fat.setText(QCoreApplication.translate("Dialog_TD", u"Fat(g)\n"
"0\n"
"0% ", None))
        self.label_water.setText(QCoreApplication.translate("Dialog_TD", u"H2O(ml)\n"
"0/0\n"
"0% ", None))
        self.button_new_train.setText(QCoreApplication.translate("Dialog_TD", u"New\n"
" training", None))
        self.button_new_aerobic.setText(QCoreApplication.translate("Dialog_TD", u"New\n"
" aerobic", None))
        self.button_new_rest.setText(QCoreApplication.translate("Dialog_TD", u"New\n"
" break", None))
        self.button_body_data.setText(QCoreApplication.translate("Dialog_TD", u"Body\n"
"data", None))
        self.button_menstrual_record.setText(QCoreApplication.translate("Dialog_TD", u"menstrual\n"
"record", None))
        self.pushButton.setText("")
    # retranslateUi

