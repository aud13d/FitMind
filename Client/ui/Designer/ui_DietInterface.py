# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FitMind_Client_DietInterface.ui'
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
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)
from ..res_rc import *

class Ui_Widget_DietInterface(object):
    def setupUi(self, Widget_DietInterface):
        if not Widget_DietInterface.objectName():
            Widget_DietInterface.setObjectName(u"Widget_DietInterface")
        Widget_DietInterface.resize(362, 700)
        Widget_DietInterface.setMinimumSize(QSize(300, 666))
        self.horizontalLayout_8 = QHBoxLayout(Widget_DietInterface)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Widget_DietInterface)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame{\n"
"background-color:rgb(236, 236, 236);\n"
"	border-top-right-radius:20px;\n"
"	border-top-left-radius:20px;\n"
"	border-bottom-right-radius:20px;\n"
"	border-bottom-left-radius:20px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QLabel{\n"
"	background-color: white; /* \u7eaf\u767d\u80cc\u666f */\n"
"	border-top-right-radius:6px;\n"
"	border-top-left-radius:6px;\n"
"	border-bottom-right-radius:6px;\n"
"	border-bottom-left-radius:6px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 6px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: white; /* \u7eaf\u767d\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"    min-width: 60px;\n"
"    min-height: 25px;\n"
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
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color: #f8f8f8;\n"
"    color: gray;\n"
"    borde"
                        "r-color: #ddd;\n"
"}\n"
"\n"
"\n"
"/* \u9009\u4e2d\u65f6\uff1a\u5b57\u4f53\u53d8\u84dd + \u53d1\u5149 */\n"
"QToolButton:checked {\n"
"    background-color: white;\n"
"    color: #0078D7; /* \u9009\u4e2d\u540e\u5b57\u4f53\u53d8\u84dd */\n"
"    font-weight: bold; /* \u52a0\u7c97 */\n"
"    text-shadow: 0px 0px 5px #4da6ff; /* \u8f7b\u5fae\u53d1\u5149\u6548\u679c */\n"
"}\n"
"\n"
"QPushButton {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 6px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: transparent; /* \u7eaf\u767d\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"    min-width: 60px;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f0f0f0; /* \u6d45\u7070\u8272\u60ac\u6d6e\u6548\u679c */\n"
"    margin-top: 2px; /* \u8f7b\u5fae\u4e0b\u79fb\uff0c\u589e\u52a0\u6309\u538b\u611f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0; /* \u6309\u4e0b\u65f6\u53d8\u6df1\u7070 */\n"
"    margin-top: 1"
                        "px; /* \u6309\u4e0b\u65f6\u8f7b\u5fae\u4e0a\u79fb */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #f8f8f8;\n"
"    color: gray;\n"
"    border-color: #ddd;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 9, 0, 16)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(16)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.button_return = QPushButton(self.frame_2)
        self.button_return.setObjectName(u"button_return")
        icon = QIcon()
        icon.addFile(u":/icons/icon/back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_return.setIcon(icon)
        self.button_return.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.button_return)

        self.button_previous = QToolButton(self.frame_2)
        self.button_previous.setObjectName(u"button_previous")
        self.button_previous.setStyleSheet(u"QToolButton{\n"
"background-color:white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.button_previous)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.button_next = QToolButton(self.frame_2)
        self.button_next.setObjectName(u"button_next")
        self.button_next.setStyleSheet(u"QToolButton{\n"
"background-color:white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.button_next)

        self.button_seeting = QPushButton(self.frame_2)
        self.button_seeting.setObjectName(u"button_seeting")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/setting.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_seeting.setIcon(icon1)
        self.button_seeting.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.button_seeting)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"#frame_3{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-top-right-radius:20px;\n"
"	border-top-left-radius:20px;\n"
"	border-bottom-right-radius:20px;\n"
"	border-bottom-left-radius:20px;\n"
"	margin-left:20px;\n"
"	margin-right:20px;\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QToolButton {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 6px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: white; /* \u7eaf\u767d\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"    min-width: 60px;\n"
"    min-height: 25px;\n"
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
"}\n"
""
                        "\n"
"QToolButton:disabled {\n"
"    background-color: #f8f8f8;\n"
"    color: gray;\n"
"    border-color: #ddd;\n"
"}\n"
"\n"
"\n"
"/* \u9009\u4e2d\u65f6\uff1a\u5b57\u4f53\u53d8\u84dd + \u53d1\u5149 */\n"
"QToolButton:checked {\n"
"    background-color: white;\n"
"    color: #0078D7; /* \u9009\u4e2d\u540e\u5b57\u4f53\u53d8\u84dd */\n"
"    font-weight: bold; /* \u52a0\u7c97 */\n"
"    text-shadow: 0px 0px 5px #4da6ff; /* \u8f7b\u5fae\u53d1\u5149\u6548\u679c */\n"
"}\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"#frame_6{\n"
"background:transparent;\n"
"margin-left: 10px;  /* \u6839\u636e\u9700\u8981\u53ef\u8c03\u6574\u6570\u503c */\n"
"margin-right: 5px;}")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.toolButton_7 = QToolButton(self.frame_6)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setStyleSheet(u"QToolButton {\n"
"    border-top-left-radius: 6px;\n"
"    border-bottom-left-radius: 6px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    padding: 2px;\n"
"    background-color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #f0f0f0; /* \u6d45\u7070\u8272\u60ac\u6d6e\u6548\u679c */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #e0e0e0; /* \u6309\u4e0b\u65f6\u53d8\u6df1\u7070 */\n"
"}")

        self.horizontalLayout_4.addWidget(self.toolButton_7)

        self.toolButton_8 = QToolButton(self.frame_6)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setStyleSheet(u"QToolButton {\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    padding: 2px;\n"
"    background-color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #f0f0f0; /* \u6d45\u7070\u8272\u60ac\u6d6e\u6548\u679c */\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.toolButton_8)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.frame_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(6, 5, 6, 10)
        self.label_diet_protein = QLabel(self.frame_3)
        self.label_diet_protein.setObjectName(u"label_diet_protein")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_diet_protein.sizePolicy().hasHeightForWidth())
        self.label_diet_protein.setSizePolicy(sizePolicy)
        self.label_diet_protein.setMinimumSize(QSize(50, 70))
        self.label_diet_protein.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_diet_protein.setStyleSheet(u"QLabel {\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 9px; /* \u5706\u89d2 */\n"
"    background-color: lightyellow; /* \u80cc\u666f\u989c\u8272 */\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"    padding: 5px; /* \u5185\u8fb9\u8ddd */\n"
"}\n"
"")
        self.label_diet_protein.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_diet_protein)

        self.label_diet_carbohydrate = QLabel(self.frame_3)
        self.label_diet_carbohydrate.setObjectName(u"label_diet_carbohydrate")
        sizePolicy.setHeightForWidth(self.label_diet_carbohydrate.sizePolicy().hasHeightForWidth())
        self.label_diet_carbohydrate.setSizePolicy(sizePolicy)
        self.label_diet_carbohydrate.setMinimumSize(QSize(50, 70))
        self.label_diet_carbohydrate.setStyleSheet(u"QLabel {\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 9px; /* \u5706\u89d2 */\n"
"    background-color: lightgreen; /* \u80cc\u666f\u989c\u8272 */\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"    padding: 5px; /* \u5185\u8fb9\u8ddd */\n"
"}\n"
"")
        self.label_diet_carbohydrate.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_diet_carbohydrate)

        self.label_diet_fat = QLabel(self.frame_3)
        self.label_diet_fat.setObjectName(u"label_diet_fat")
        sizePolicy.setHeightForWidth(self.label_diet_fat.sizePolicy().hasHeightForWidth())
        self.label_diet_fat.setSizePolicy(sizePolicy)
        self.label_diet_fat.setMinimumSize(QSize(50, 70))
        self.label_diet_fat.setStyleSheet(u"QLabel {\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 9px; /* \u5706\u89d2 */\n"
"\n"
"	\n"
"	background-color: rgb(255, 144, 155);\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"    padding: 5px; /* \u5185\u8fb9\u8ddd */\n"
"}\n"
"")
        self.label_diet_fat.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_diet_fat)

        self.label_diet_water = QLabel(self.frame_3)
        self.label_diet_water.setObjectName(u"label_diet_water")
        sizePolicy.setHeightForWidth(self.label_diet_water.sizePolicy().hasHeightForWidth())
        self.label_diet_water.setSizePolicy(sizePolicy)
        self.label_diet_water.setMinimumSize(QSize(50, 70))
        self.label_diet_water.setStyleSheet(u"QLabel {\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 9px; /* \u5706\u89d2 */\n"
"    background-color: lightblue; /* \u80cc\u666f\u989c\u8272 */\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"    padding: 5px; /* \u5185\u8fb9\u8ddd */\n"
"}\n"
"")
        self.label_diet_water.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_diet_water)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {              /* \u4e3b\u5bb9\u5668 */\n"
"    border: none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 362, 452))
        self.horizontalLayout_9 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QToolButton {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 6px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: white; /* \u7eaf\u767d\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"    min-width: 60px;\n"
"    min-height: 25px;\n"
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
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color: #f8f8f8;\n"
"    color: gray;\n"
"    border-color: #ddd;\n"
"}\n"
"\n"
"\n"
"/* \u9009\u4e2d\u65f6\uff1a\u5b57\u4f53\u53d8\u84dd + \u53d1\u5149 */\n"
"QToolButton:checked {\n"
"    background-color: white;\n"
"    color: #0078D7; /* \u9009\u4e2d\u540e\u5b57\u4f53\u53d8"
                        "\u84dd */\n"
"    font-weight: bold; /* \u52a0\u7c97 */\n"
"    text-shadow: 0px 0px 5px #4da6ff; /* \u8f7b\u5fae\u53d1\u5149\u6548\u679c */\n"
"}\n"
"\n"
"")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(16)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 0, 20, -1)
        self.button_carbonCycleSetting = QToolButton(self.frame_7)
        self.button_carbonCycleSetting.setObjectName(u"button_carbonCycleSetting")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_carbonCycleSetting.sizePolicy().hasHeightForWidth())
        self.button_carbonCycleSetting.setSizePolicy(sizePolicy1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/xunhuan.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_carbonCycleSetting.setIcon(icon2)
        self.button_carbonCycleSetting.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_3.addWidget(self.button_carbonCycleSetting)

        self.button_Menu = QToolButton(self.frame_7)
        self.button_Menu.setObjectName(u"button_Menu")
        sizePolicy1.setHeightForWidth(self.button_Menu.sizePolicy().hasHeightForWidth())
        self.button_Menu.setSizePolicy(sizePolicy1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/shipu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_Menu.setIcon(icon3)
        self.button_Menu.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_3.addWidget(self.button_Menu)

        self.button_foodRecommendation = QToolButton(self.frame_7)
        self.button_foodRecommendation.setObjectName(u"button_foodRecommendation")
        sizePolicy1.setHeightForWidth(self.button_foodRecommendation.sizePolicy().hasHeightForWidth())
        self.button_foodRecommendation.setSizePolicy(sizePolicy1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/tuijianma.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_foodRecommendation.setIcon(icon4)
        self.button_foodRecommendation.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_3.addWidget(self.button_foodRecommendation)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_5.addWidget(self.frame_8)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 9)

        self.horizontalLayout_9.addWidget(self.frame_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	background:white;\n"
"	border-bottom-right-radius:20px;\n"
"	border-bottom-left-radius:20px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\"; \n"
"    qproperty-alignment: AlignLeft; /* \u6587\u5b57\u5de6\u5bf9\u9f50 */\n"
"    padding-left: 0px; /* \u786e\u4fdd\u7d27\u8d34\u5de6\u8fb9 */\n"
"    border-radius: 6px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: transparent; \n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"    min-width: 16px;\n"
"    min-height: 16px;\n"
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
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color: #f8f8f8;\n"
"    color"
                        ": gray;\n"
"    border-color: #ddd;\n"
"}\n"
"\n"
"/* \u9009\u4e2d\u65f6\uff1a\u5b57\u4f53\u53d8\u84dd + \u53d1\u5149 */\n"
"QToolButton:checked {\n"
"    background-color: transparent;\n"
"    color: #0078D7; /* \u9009\u4e2d\u540e\u5b57\u4f53\u53d8\u84dd */\n"
"    font-weight: bold; /* \u52a0\u7c97 */\n"
"    text-shadow: 0px 0px 5px #4da6ff; /* \u8f7b\u5fae\u53d1\u5149\u6548\u679c */\n"
"}\n"
"")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 5)
        self.button_diet_breakfast = QToolButton(self.frame_5)
        self.button_diet_breakfast.setObjectName(u"button_diet_breakfast")
        self.button_diet_breakfast.setMinimumSize(QSize(16, 16))
        self.button_diet_breakfast.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icon/zaocan.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_diet_breakfast.setIcon(icon5)
        self.button_diet_breakfast.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_diet_breakfast)

        self.button_diet_lunch = QToolButton(self.frame_5)
        self.button_diet_lunch.setObjectName(u"button_diet_lunch")
        self.button_diet_lunch.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icon/wucan.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_diet_lunch.setIcon(icon6)
        self.button_diet_lunch.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_diet_lunch)

        self.button_diet_dinner = QToolButton(self.frame_5)
        self.button_diet_dinner.setObjectName(u"button_diet_dinner")
        self.button_diet_dinner.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icon/hanbao.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_diet_dinner.setIcon(icon7)
        self.button_diet_dinner.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_diet_dinner)

        self.button_diet_extra_meal = QToolButton(self.frame_5)
        self.button_diet_extra_meal.setObjectName(u"button_diet_extra_meal")
        self.button_diet_extra_meal.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icon/jiangmianbaoregou.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_diet_extra_meal.setIcon(icon8)
        self.button_diet_extra_meal.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_diet_extra_meal)

        self.button_diet_drink = QToolButton(self.frame_5)
        self.button_diet_drink.setObjectName(u"button_diet_drink")
        self.button_diet_drink.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icon/yinshui.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_diet_drink.setIcon(icon9)
        self.button_diet_drink.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_diet_drink)

        self.button_diet_statistics = QToolButton(self.frame_5)
        self.button_diet_statistics.setObjectName(u"button_diet_statistics")
        self.button_diet_statistics.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icon/tizhong.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_diet_statistics.setIcon(icon10)
        self.button_diet_statistics.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_diet_statistics)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.horizontalLayout_8.addWidget(self.frame)


        self.retranslateUi(Widget_DietInterface)
        self.button_return.clicked.connect(Widget_DietInterface.close)

        QMetaObject.connectSlotsByName(Widget_DietInterface)
    # setupUi

    def retranslateUi(self, Widget_DietInterface):
        Widget_DietInterface.setWindowTitle(QCoreApplication.translate("Widget_DietInterface", u"Form", None))
        self.button_return.setText("")
        self.button_previous.setText(QCoreApplication.translate("Widget_DietInterface", u"<", None))
        self.label.setText(QCoreApplication.translate("Widget_DietInterface", u"Today", None))
        self.button_next.setText(QCoreApplication.translate("Widget_DietInterface", u">", None))
        self.button_seeting.setText("")
        self.label_2.setText(QCoreApplication.translate("Widget_DietInterface", u"0", None))
        self.toolButton_7.setText(QCoreApplication.translate("Widget_DietInterface", u"Set Template", None))
        self.toolButton_8.setText(QCoreApplication.translate("Widget_DietInterface", u"Share", None))
        self.label_diet_protein.setText(QCoreApplication.translate("Widget_DietInterface", u"Pro(g)\n"
"0\n"
"0% ", None))
        self.label_diet_carbohydrate.setText(QCoreApplication.translate("Widget_DietInterface", u"Carbs(g)\n"
"0\n"
"0% ", None))
        self.label_diet_fat.setText(QCoreApplication.translate("Widget_DietInterface", u"Fat(g)\n"
"0\n"
"0% ", None))
        self.label_diet_water.setText(QCoreApplication.translate("Widget_DietInterface", u"H2O(ml)\n"
"0/0\n"
"0% ", None))
        self.button_carbonCycleSetting.setText(QCoreApplication.translate("Widget_DietInterface", u" C-Cycle", None))
        self.button_Menu.setText(QCoreApplication.translate("Widget_DietInterface", u"Menu+", None))
        self.button_foodRecommendation.setText(QCoreApplication.translate("Widget_DietInterface", u"Rec", None))
        self.button_diet_breakfast.setText(QCoreApplication.translate("Widget_DietInterface", u"breakfast", None))
        self.button_diet_lunch.setText(QCoreApplication.translate("Widget_DietInterface", u"lunch", None))
        self.button_diet_dinner.setText(QCoreApplication.translate("Widget_DietInterface", u"dinner", None))
        self.button_diet_extra_meal.setText(QCoreApplication.translate("Widget_DietInterface", u"extra-meal", None))
        self.button_diet_drink.setText(QCoreApplication.translate("Widget_DietInterface", u"drink", None))
        self.button_diet_statistics.setText(QCoreApplication.translate("Widget_DietInterface", u"statistics", None))
    # retranslateUi

