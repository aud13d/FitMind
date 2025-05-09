# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FitMind_Client_MainInterface.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCalendarWidget, QFrame,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSplitter,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)
from ..res_rc import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(362, 700)
        MainWindow.setMinimumSize(QSize(300, 666))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_9 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 666))
        self.frame.setStyleSheet(u"#frame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-top-right-radius:20px;\n"
"	border-top-left-radius:20px;\n"
"	border-bottom-right-radius:20px;\n"
"	border-bottom-left-radius:20px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_2)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page_train = QWidget()
        self.page_train.setObjectName(u"page_train")
        self.page_train.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_5 = QVBoxLayout(self.page_train)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 4, 3, 0)
        self.horizontalSpacer = QSpacerItem(90, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.button_friend = QPushButton(self.page_train)
        self.button_friend.setObjectName(u"button_friend")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_friend.sizePolicy().hasHeightForWidth())
        self.button_friend.setSizePolicy(sizePolicy1)
        self.button_friend.setMinimumSize(QSize(16, 16))
        self.button_friend.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 6px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: white; /* \u7eaf\u767d\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"    min-width: 16px;\n"
"    min-height: 16px;\n"
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
"    border-color: #ddd;\n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icon/user-multiple-group--close-geometric-human-multipl.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_friend.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.button_friend)

        self.pushButton = QPushButton(self.page_train)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(16, 16))
        self.pushButton.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 6px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: white; /* \u7eaf\u767d\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"    min-width: 16px;\n"
"    min-height: 16px;\n"
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
"    border-color: #ddd;\n"
"}\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/delete-1--remove-add-button-buttons-delete-cross-x.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.horizontalLayout_3.setStretch(0, 8)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.frame_10 = QFrame(self.page_train)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_10.setLineWidth(0)
        self.verticalLayout_11 = QVBoxLayout(self.frame_10)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_10)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(0, 0))
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
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 340, 650))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.horizontalLayout_6 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setStyleSheet(u"\n"
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
"    color: gray;\n"
"    border-color: #ddd;\n"
"}\n"
"\n"
"/* \u9009\u4e2d\u65f6\uff1a\u5b57\u4f53\u53d8\u84dd + \u53d1"
                        "\u5149 */\n"
"QToolButton:checked {\n"
"    background-color: transparent;\n"
"    color: #0078D7; /* \u9009\u4e2d\u540e\u5b57\u4f53\u53d8\u84dd */\n"
"    font-weight: bold; /* \u52a0\u7c97 */\n"
"    text-shadow: 0px 0px 5px #4da6ff; /* \u8f7b\u5fae\u53d1\u5149\u6548\u679c */\n"
"}\n"
"")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_4.setLineWidth(0)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, -1, 0)
        self.frame_diet_record = QFrame(self.frame_4)
        self.frame_diet_record.setObjectName(u"frame_diet_record")
        sizePolicy.setHeightForWidth(self.frame_diet_record.sizePolicy().hasHeightForWidth())
        self.frame_diet_record.setSizePolicy(sizePolicy)
        self.frame_diet_record.setMinimumSize(QSize(0, 200))
        self.frame_diet_record.setStyleSheet(u"font: 700 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.frame_diet_record.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_diet_record.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_diet_record)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_train_diet_record = QLabel(self.frame_diet_record)
        self.label_train_diet_record.setObjectName(u"label_train_diet_record")
        sizePolicy3.setHeightForWidth(self.label_train_diet_record.sizePolicy().hasHeightForWidth())
        self.label_train_diet_record.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.label_train_diet_record)

        self.frame_6 = QFrame(self.frame_diet_record)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(8)
        sizePolicy4.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy4)
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(0, 10, 331, 216))
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setStyleSheet(u"#frame_13{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-top-right-radius:40px;\n"
"	border-top-left-radius:40px;\n"
"	border-bottom-right-radius:40px;\n"
"	border-bottom-left-radius:40px;\n"
"}\n"
"\n"
"QToolButton{\n"
"	font:9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_13)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_train_already_eaten = QLabel(self.frame_13)
        self.label_train_already_eaten.setObjectName(u"label_train_already_eaten")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_train_already_eaten.sizePolicy().hasHeightForWidth())
        self.label_train_already_eaten.setSizePolicy(sizePolicy5)
        self.label_train_already_eaten.setMinimumSize(QSize(0, 35))
        self.label_train_already_eaten.setMaximumSize(QSize(16777215, 35))
        self.label_train_already_eaten.setStyleSheet(u"font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_train_already_eaten.setMargin(8)

        self.verticalLayout_2.addWidget(self.label_train_already_eaten)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(6, 5, 6, 10)
        self.label_train_protein = QLabel(self.frame_13)
        self.label_train_protein.setObjectName(u"label_train_protein")
        sizePolicy1.setHeightForWidth(self.label_train_protein.sizePolicy().hasHeightForWidth())
        self.label_train_protein.setSizePolicy(sizePolicy1)
        self.label_train_protein.setMinimumSize(QSize(50, 70))
        self.label_train_protein.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_train_protein.setStyleSheet(u"QLabel {\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 9px; /* \u5706\u89d2 */\n"
"    background-color: lightyellow; /* \u80cc\u666f\u989c\u8272 */\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"    padding: 5px; /* \u5185\u8fb9\u8ddd */\n"
"}\n"
"")
        self.label_train_protein.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_train_protein)

        self.label_train_carbohydrate = QLabel(self.frame_13)
        self.label_train_carbohydrate.setObjectName(u"label_train_carbohydrate")
        sizePolicy1.setHeightForWidth(self.label_train_carbohydrate.sizePolicy().hasHeightForWidth())
        self.label_train_carbohydrate.setSizePolicy(sizePolicy1)
        self.label_train_carbohydrate.setMinimumSize(QSize(50, 70))
        self.label_train_carbohydrate.setStyleSheet(u"QLabel {\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 9px; /* \u5706\u89d2 */\n"
"    background-color: lightgreen; /* \u80cc\u666f\u989c\u8272 */\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"    padding: 5px; /* \u5185\u8fb9\u8ddd */\n"
"}\n"
"")
        self.label_train_carbohydrate.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_train_carbohydrate)

        self.label_train_fat = QLabel(self.frame_13)
        self.label_train_fat.setObjectName(u"label_train_fat")
        sizePolicy1.setHeightForWidth(self.label_train_fat.sizePolicy().hasHeightForWidth())
        self.label_train_fat.setSizePolicy(sizePolicy1)
        self.label_train_fat.setMinimumSize(QSize(50, 70))
        self.label_train_fat.setStyleSheet(u"QLabel {\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 9px; /* \u5706\u89d2 */\n"
"\n"
"	\n"
"	background-color: rgb(255, 144, 155);\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"    padding: 5px; /* \u5185\u8fb9\u8ddd */\n"
"}\n"
"")
        self.label_train_fat.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_train_fat)

        self.label_train_water = QLabel(self.frame_13)
        self.label_train_water.setObjectName(u"label_train_water")
        sizePolicy1.setHeightForWidth(self.label_train_water.sizePolicy().hasHeightForWidth())
        self.label_train_water.setSizePolicy(sizePolicy1)
        self.label_train_water.setMinimumSize(QSize(50, 70))
        self.label_train_water.setStyleSheet(u"QLabel {\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 9px; /* \u5706\u89d2 */\n"
"    background-color: lightblue; /* \u80cc\u666f\u989c\u8272 */\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"    padding: 5px; /* \u5185\u8fb9\u8ddd */\n"
"}\n"
"")
        self.label_train_water.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_train_water)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 10, -1, 10)
        self.button_train_breakfast = QToolButton(self.frame_13)
        self.button_train_breakfast.setObjectName(u"button_train_breakfast")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/zaocan.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_train_breakfast.setIcon(icon2)
        self.button_train_breakfast.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_8.addWidget(self.button_train_breakfast)

        self.button_train_lunch = QToolButton(self.frame_13)
        self.button_train_lunch.setObjectName(u"button_train_lunch")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/wucan.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_train_lunch.setIcon(icon3)
        self.button_train_lunch.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_8.addWidget(self.button_train_lunch)

        self.button_train_dinner = QToolButton(self.frame_13)
        self.button_train_dinner.setObjectName(u"button_train_dinner")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/hanbao.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_train_dinner.setIcon(icon4)
        self.button_train_dinner.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_8.addWidget(self.button_train_dinner)

        self.button_train_extra_meal = QToolButton(self.frame_13)
        self.button_train_extra_meal.setObjectName(u"button_train_extra_meal")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icon/jiangmianbaoregou.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_train_extra_meal.setIcon(icon5)
        self.button_train_extra_meal.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_8.addWidget(self.button_train_extra_meal)

        self.button_train_drink = QToolButton(self.frame_13)
        self.button_train_drink.setObjectName(u"button_train_drink")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icon/yinshui.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_train_drink.setIcon(icon6)
        self.button_train_drink.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_8.addWidget(self.button_train_drink)

        self.button_train_weight = QToolButton(self.frame_13)
        self.button_train_weight.setObjectName(u"button_train_weight")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icon/tizhong.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_train_weight.setIcon(icon7)
        self.button_train_weight.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout_8.addWidget(self.button_train_weight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_10.addWidget(self.frame_diet_record)

        self.frame_plan_model = QFrame(self.frame_4)
        self.frame_plan_model.setObjectName(u"frame_plan_model")
        sizePolicy.setHeightForWidth(self.frame_plan_model.sizePolicy().hasHeightForWidth())
        self.frame_plan_model.setSizePolicy(sizePolicy)
        self.frame_plan_model.setMinimumSize(QSize(0, 0))
        self.frame_plan_model.setStyleSheet(u"font: 700 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"\n"
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
"    border-color: #ddd;\n"
"}\n"
"\n"
"\n"
"/* \u9009\u4e2d\u65f6\uff1a\u5b57\u4f53\u53d8\u84dd + \u53d1\u5149 */\n"
"QToolButton:checked {\n"
"    background-color: white;\n"
""
                        "    color: #0078D7; /* \u9009\u4e2d\u540e\u5b57\u4f53\u53d8\u84dd */\n"
"    font-weight: bold; /* \u52a0\u7c97 */\n"
"    text-shadow: 0px 0px 5px #4da6ff; /* \u8f7b\u5fae\u53d1\u5149\u6548\u679c */\n"
"}\n"
"\n"
"")
        self.frame_plan_model.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_plan_model.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_plan_model.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_plan_model)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.frame_plan_model)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_2.setHandleWidth(0)
        self.button_train_official_plan = QToolButton(self.splitter_2)
        self.button_train_official_plan.setObjectName(u"button_train_official_plan")
        self.button_train_official_plan.setCheckable(True)
        self.button_train_official_plan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        self.splitter_2.addWidget(self.button_train_official_plan)
        self.button_train_personal_plan = QToolButton(self.splitter_2)
        self.button_train_personal_plan.setObjectName(u"button_train_personal_plan")
        self.button_train_personal_plan.setCheckable(True)
        self.splitter_2.addWidget(self.button_train_personal_plan)

        self.verticalLayout_4.addWidget(self.splitter_2)

        self.stackedWidget_2 = QStackedWidget(self.frame_plan_model)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_official_plan = QWidget()
        self.page_official_plan.setObjectName(u"page_official_plan")
        self.verticalLayout_8 = QVBoxLayout(self.page_official_plan)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 9, 0, 0)
        self.frame_8 = QFrame(self.page_official_plan)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy4.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy4)
        self.frame_8.setStyleSheet(u"font: 290 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.splitter_3 = QSplitter(self.frame_8)
        self.splitter_3.setObjectName(u"splitter_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.splitter_3.sizePolicy().hasHeightForWidth())
        self.splitter_3.setSizePolicy(sizePolicy6)
        self.splitter_3.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_3.setHandleWidth(0)
        self.button_train_plan1 = QToolButton(self.splitter_3)
        self.button_train_plan1.setObjectName(u"button_train_plan1")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.button_train_plan1.sizePolicy().hasHeightForWidth())
        self.button_train_plan1.setSizePolicy(sizePolicy7)
        self.button_train_plan1.setCheckable(True)
        self.splitter_3.addWidget(self.button_train_plan1)
        self.button_train_plan2 = QToolButton(self.splitter_3)
        self.button_train_plan2.setObjectName(u"button_train_plan2")
        sizePolicy7.setHeightForWidth(self.button_train_plan2.sizePolicy().hasHeightForWidth())
        self.button_train_plan2.setSizePolicy(sizePolicy7)
        self.button_train_plan2.setCheckable(True)
        self.splitter_3.addWidget(self.button_train_plan2)
        self.button_train_plan3 = QToolButton(self.splitter_3)
        self.button_train_plan3.setObjectName(u"button_train_plan3")
        self.button_train_plan3.setCheckable(True)
        self.splitter_3.addWidget(self.button_train_plan3)
        self.button_train_plan4 = QToolButton(self.splitter_3)
        self.button_train_plan4.setObjectName(u"button_train_plan4")
        self.button_train_plan4.setCheckable(True)
        self.splitter_3.addWidget(self.button_train_plan4)

        self.verticalLayout_7.addWidget(self.splitter_3)

        self.stackedWidget_3 = QStackedWidget(self.frame_8)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setLineWidth(0)
        self.page_plan1 = QWidget()
        self.page_plan1.setObjectName(u"page_plan1")
        self.stackedWidget_3.addWidget(self.page_plan1)
        self.page_plan2 = QWidget()
        self.page_plan2.setObjectName(u"page_plan2")
        self.stackedWidget_3.addWidget(self.page_plan2)

        self.verticalLayout_7.addWidget(self.stackedWidget_3)


        self.verticalLayout_8.addWidget(self.frame_8)

        self.stackedWidget_2.addWidget(self.page_official_plan)
        self.page_personal_plan = QWidget()
        self.page_personal_plan.setObjectName(u"page_personal_plan")
        self.verticalLayout_6 = QVBoxLayout(self.page_personal_plan)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.page_personal_plan)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_6.addWidget(self.frame_9)

        self.stackedWidget_2.addWidget(self.page_personal_plan)

        self.verticalLayout_4.addWidget(self.stackedWidget_2)


        self.verticalLayout_10.addWidget(self.frame_plan_model)


        self.horizontalLayout_6.addWidget(self.frame_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 13)
        self.stackedWidget.addWidget(self.page_train)
        self.page_sports = QWidget()
        self.page_sports.setObjectName(u"page_sports")
        self.scrollArea_2 = QScrollArea(self.page_sports)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(9, 9, 324, 61))
        self.scrollArea_2.setStyleSheet(u"QWidget {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font: 550 9pt \"\u5fae\u8f6f\u96c5\u9ed1\"; \n"
"    border-radius: 6px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"	background-color: #f0f0f0;\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e0e0e0; /* \u6d45\u7070\u8272\u60ac\u6d6e\u6548\u679c */\n"
"    padding-bottom: 2px; /* \u8f7b\u5fae\u4e0b\u79fb\uff0c\u589e\u52a0\u6309\u538b\u611f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #d0d0d0; /* \u66f4\u6df1\u7684\u7070\u8272\uff0c\u6309\u4e0b\u6548\u679c */\n"
"    padding-bottom: 1px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #f8f8f8;\n"
"    color: gray;\n"
"    border-color: #ddd;\n"
"}\n"
"\n"
"\n"
"QScrollArea {\n"
"	border:none;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 4px;\n"
"    margin: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle"
                        ":vertical {\n"
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
"    background: rgba(100, 100, 100, 0.8);\n"
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
        self.scrollArea_2.setWidgetResizable(False)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 945, 57))
        self.layoutWidget = QWidget(self.scrollAreaWidgetContents_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(9, 11, 931, 37))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.button_sports_running_outside = QPushButton(self.layoutWidget)
        self.button_sports_running_outside.setObjectName(u"button_sports_running_outside")
        self.button_sports_running_outside.setMinimumSize(QSize(125, 35))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icon/benpao.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_sports_running_outside.setIcon(icon8)
        self.button_sports_running_outside.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.button_sports_running_outside)

        self.button_sports_running_inside = QPushButton(self.layoutWidget)
        self.button_sports_running_inside.setObjectName(u"button_sports_running_inside")
        self.button_sports_running_inside.setMinimumSize(QSize(125, 35))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icon/shineipaobu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_sports_running_inside.setIcon(icon9)
        self.button_sports_running_inside.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.button_sports_running_inside)

        self.button_sports_walk = QPushButton(self.layoutWidget)
        self.button_sports_walk.setObjectName(u"button_sports_walk")
        self.button_sports_walk.setMinimumSize(QSize(125, 35))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icon/walk.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_sports_walk.setIcon(icon10)
        self.button_sports_walk.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.button_sports_walk)

        self.button_sports_riding = QPushButton(self.layoutWidget)
        self.button_sports_riding.setObjectName(u"button_sports_riding")
        self.button_sports_riding.setMinimumSize(QSize(125, 35))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icon/\u9a91\u884c.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_sports_riding.setIcon(icon11)
        self.button_sports_riding.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.button_sports_riding)

        self.button_sports_fitness = QPushButton(self.layoutWidget)
        self.button_sports_fitness.setObjectName(u"button_sports_fitness")
        self.button_sports_fitness.setMinimumSize(QSize(125, 35))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icon/ticao.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_sports_fitness.setIcon(icon12)
        self.button_sports_fitness.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.button_sports_fitness)

        self.button_sports_jump_rope = QPushButton(self.layoutWidget)
        self.button_sports_jump_rope.setObjectName(u"button_sports_jump_rope")
        self.button_sports_jump_rope.setMinimumSize(QSize(125, 35))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icon/tiaosheng.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_sports_jump_rope.setIcon(icon13)
        self.button_sports_jump_rope.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.button_sports_jump_rope)

        self.button_sports_more = QPushButton(self.layoutWidget)
        self.button_sports_more.setObjectName(u"button_sports_more")
        self.button_sports_more.setMinimumSize(QSize(125, 35))
        icon14 = QIcon()
        icon14.addFile(u":/icons/icon/\u66f4\u591a\u3001\u5206\u7c7b.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_sports_more.setIcon(icon14)
        self.button_sports_more.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.button_sports_more)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget.addWidget(self.page_sports)
        self.page_history = QWidget()
        self.page_history.setObjectName(u"page_history")
        sizePolicy.setHeightForWidth(self.page_history.sizePolicy().hasHeightForWidth())
        self.page_history.setSizePolicy(sizePolicy)
        self.verticalLayout_12 = QVBoxLayout(self.page_history)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.page_history)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(1)
        sizePolicy8.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy8)
        self.frame_11.setStyleSheet(u"#frame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-top-right-radius:20px;\n"
"	border-top-left-radius:20px;\n"
"	border-bottom-right-radius:20px;\n"
"	border-bottom-left-radius:20px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    font: 700 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 6px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: white; /* \u7eaf\u767d\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"    min-width: 60px;\n"
"    min-height: 60px;\n"
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
"    border-color: "
                        "#ddd;\n"
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
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_11.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 10, 5, 0)
        self.button_history_history = QToolButton(self.frame_11)
        self.button_history_history.setObjectName(u"button_history_history")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.button_history_history.sizePolicy().hasHeightForWidth())
        self.button_history_history.setSizePolicy(sizePolicy9)
        self.button_history_history.setMinimumSize(QSize(60, 60))
        self.button_history_history.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.button_history_history)

        self.button_history_statistics = QToolButton(self.frame_11)
        self.button_history_statistics.setObjectName(u"button_history_statistics")
        sizePolicy9.setHeightForWidth(self.button_history_statistics.sizePolicy().hasHeightForWidth())
        self.button_history_statistics.setSizePolicy(sizePolicy9)
        self.button_history_statistics.setMinimumSize(QSize(60, 60))
        self.button_history_statistics.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.button_history_statistics)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.page_history)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(10)
        sizePolicy10.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy10)
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.calendarWidget = QCalendarWidget(self.frame_12)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setStyleSheet(u"/*\u9876\u90e8\u5bfc\u822a\u533a\u57df*/\n"
"#qt_calendar_navigationbar {\n"
"    background-color: white;\n"
"    min-height: 10px;\n"
"	max-height: 1000px;\n"
"}\n"
"\n"
"\n"
"/*\u4e0a\u4e00\u4e2a\u6708\u6309\u94ae\u548c\u4e0b\u4e00\u4e2a\u6708\u6309\u94ae*/\n"
"#qt_calendar_prevmonth, #qt_calendar_nextmonth {\n"
"	padding:0px;\n"
"    border: none; /*\u53bb\u6389\u8fb9\u6846*/\n"
"    color: black;\n"
"	min-width: 20px;\n"
"    max-width: 20px;\n"
"    min-height: 16px;\n"
"    max-height: 16px;\n"
"    border-radius: 6px; /*\u770b\u6765\u8fd1\u4f3c\u692d\u5706*/\n"
"    font-weight: bold; /*\u5b57\u4f53\u52a0\u7c97*/\n"
"	    qproperty-icon: none; /*\u53bb\u6389\u9ed8\u8ba4\u7684\u65b9\u5411\u952e\u56fe\u7247\uff0c\u5f53\u7136\u4e5f\u53ef\u4ee5\u81ea\u5b9a\u4e49*/\n"
"    background-color: transparent;/*\u80cc\u666f\u989c\u8272\u900f\u660e*/\n"
"}\n"
"\n"
"#qt_calendar_prevmonth {\n"
"	font-size:20px;\n"
"    qproperty-text: \"<\"; /*\u4fee\u6539\u6309\u94ae\u7684\u6587\u5b57*/\n"
"}\n"
"#qt_calendar_nextm"
                        "onth {\n"
"font-size:20px;\n"
"    qproperty-text: \">\";\n"
"}\n"
"#qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {\n"
"    background-color: rgba(0, 0, 0, 100);\n"
"}\n"
"#qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {\n"
"    background-color: rgba(0, 0, 0, 100);\n"
"}\n"
"\n"
"\n"
"/*\u5e74,\u6708\u63a7\u4ef6*/\n"
"#qt_calendar_yearbutton, #qt_calendar_monthbutton {\n"
"    color: black;\n"
"    margin: 10px;\n"
"    min-width: 60px;\n"
"    border-radius: 30px;\n"
"\n"
"	font: 700 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"#qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {\n"
"    background-color: rgba(225, 225, 225, 100);\n"
"}\n"
"#qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {\n"
"    background-color: rgba(235, 235, 235, 100);\n"
"}\n"
"\n"
"\n"
"/*\u5e74\u4efd\u8f93\u5165\u6846*/\n"
"#qt_calendar_yearedit {\n"
"    min-width: 50px;\n"
"    color: white;\n"
"    background: transparent;/*\u8ba9\u8f93\u5165\u6846\u80cc\u666f\u900f\u660e*/"
                        "\n"
"}\n"
"#qt_calendar_yearedit::up-button { /*\u5f80\u4e0a\u7684\u6309\u94ae*/\n"
"    width: 20px;\n"
"    subcontrol-position: right;/*\u79fb\u52a8\u5230\u53f3\u8fb9*/\n"
"}\n"
"#qt_calendar_yearedit::down-button { /*\u5f80\u4e0b\u7684\u6309\u94ae*/\n"
"    width: 20px;\n"
"    subcontrol-position: left; /*\u79fb\u52a8\u5230\u5de6\u8fb9\u53bb*/\n"
"}\n"
"\n"
"\n"
"/* \u6708\u4efd\u9009\u62e9\u83dc\u5355 */\n"
"QCalendarWidget QToolButton QMenu {\n"
"     background-color: white;\n"
"}\n"
"\n"
"/* \u83dc\u5355\u9879\u6837\u5f0f */\n"
"QCalendarWidget QToolButton QMenu::item {\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton QMenu::item:selected:enabled {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"/* \u53bb\u6389\u6708\u4efd\u9009\u62e9\u5c0f\u7bad\u5934 */\n"
"QCalendarWidget QToolButton::menu-indicator {\n"
"	image: none;\n"
"    subcontrol-position: right center;\n"
"}\n"
"\n"
"\n"
"/*\u4e0b\u65b9\u7684\u65e5\u5386\u8868\u683c*/\n"
"#qt_calendar_calendarview::item:select"
                        "ed {\n"
"    background-color: rgb(0, 188, 212); /* \u9009\u4e2d\u7684\u80cc\u666f\u989c\u8272 */\n"
"    color: white; /* \u5b57\u4f53\u53d8\u767d */\n"
"    border-radius: 15px; /* \u8ba9\u80cc\u666f\u53d8\u6210\u5706\u5f62 */\n"
"    padding: 0px 0px; /* \u8c03\u6574\u5185\u8fb9\u8ddd\uff1a\u4e0a\u4e0b 2px\uff0c\u5de6\u53f3 8px */\n"
"    margin: 16px 6px; /* \u4e0a\u4e0b\u51cf\u5c11\u95f4\u8ddd */\n"
"	outline: none;\n"
"}\n"
"\n"
"#qt_calendar_calendarview {\n"
"    outline: none; /* \u53bb\u6389\u9009\u4e2d\u540e\u7684\u865a\u7ebf\u6846 */\n"
"}\n"
"\n"
"/* \u65e5\u5386\u680f */\n"
"QCalendarWidget QTableView {\n"
"	font:12px \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	background-color: white; /* \u80cc\u666f\u989c\u8272 */\n"
" max-height: 450px;\n"
"}\n"
"\n"
"\n"
"/* \u8c03\u6574\u9009\u4e2d\u65e5\u671f\u7684\u6837\u5f0f */\n"
"QCalendarWidget QAbstractItemView::item:selected {\n"
"    background-color: rgb(0, 188, 212); /* \u9009\u4e2d\u7684\u80cc\u666f\u989c\u8272 */\n"
"    color: white; /* \u5b57\u4f53\u53d8"
                        "\u767d */\n"
"    border-radius: 15px; /* \u5706\u5f62\u80cc\u666f */\n"
"    padding: 2px;\n"
"}\n"
"")
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setSelectionMode(QCalendarWidget.SelectionMode.NoSelection)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)

        self.horizontalLayout_5.addWidget(self.calendarWidget)


        self.verticalLayout_12.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.page_history)
        self.page_user = QWidget()
        self.page_user.setObjectName(u"page_user")
        self.stackedWidget.addWidget(self.page_user)

        self.verticalLayout_13.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"\n"
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
"    border-color: #ddd;\n"
"}\n"
"\n"
"\n"
"/* \u9009\u4e2d\u65f6\uff1a\u5b57\u4f53\u53d8\u84dd + \u53d1\u5149 */\n"
"QToolButton:checked {\n"
"    background-color: white;\n"
"    color: #0078D7; /* \u9009\u4e2d\u540e\u5b57"
                        "\u4f53\u53d8\u84dd */\n"
"    font-weight: bold; /* \u52a0\u7c97 */\n"
"    text-shadow: 0px 0px 5px #4da6ff; /* \u8f7b\u5fae\u53d1\u5149\u6548\u679c */\n"
"}\n"
"\n"
"")
        self.frame_3.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.button_train = QToolButton(self.frame_3)
        self.button_train.setObjectName(u"button_train")
        sizePolicy9.setHeightForWidth(self.button_train.sizePolicy().hasHeightForWidth())
        self.button_train.setSizePolicy(sizePolicy9)
        self.button_train.setMinimumSize(QSize(60, 25))
        icon15 = QIcon()
        icon15.addFile(u":/icons/icon/xunlianjihua.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon15.addFile(u":/icons/icon/xunlianjihua.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_train.setIcon(icon15)
        self.button_train.setIconSize(QSize(16, 16))
        self.button_train.setCheckable(True)
        self.button_train.setChecked(False)
        self.button_train.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_train)

        self.button_sports = QToolButton(self.frame_3)
        self.button_sports.setObjectName(u"button_sports")
        sizePolicy9.setHeightForWidth(self.button_sports.sizePolicy().hasHeightForWidth())
        self.button_sports.setSizePolicy(sizePolicy9)
        icon16 = QIcon()
        icon16.addFile(u":/icons/icon/dongzuo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon16.addFile(u":/icons/icon/dongzuo.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_sports.setIcon(icon16)
        self.button_sports.setCheckable(True)
        self.button_sports.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_sports)

        self.button_TrainAndDiet = QPushButton(self.frame_3)
        self.button_TrainAndDiet.setObjectName(u"button_TrainAndDiet")
        sizePolicy9.setHeightForWidth(self.button_TrainAndDiet.sizePolicy().hasHeightForWidth())
        self.button_TrainAndDiet.setSizePolicy(sizePolicy9)
        self.button_TrainAndDiet.setMinimumSize(QSize(62, 42))
        self.button_TrainAndDiet.setMaximumSize(QSize(16777215, 16777215))
        self.button_TrainAndDiet.setStyleSheet(u"QPushButton {\n"
"    font: 700 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 18px;\n"
"\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(123, 203, 255, 230),\n"
"        stop:1 rgba(185, 159, 255, 220)\n"
"    );\n"
"    color: white;\n"
"    min-width: 60px;\n"
"    min-height: 40px;\n"
"\n"
"    box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.35);\n"
"    outline: none;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(105, 180, 255, 255),\n"
"        stop:1 rgba(170, 140, 255, 235)\n"
"    );\n"
"    padding-bottom: 2px;\n"
"    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.25);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(85, 160, 235, 255),\n"
"        stop:1 rgba(150, 12"
                        "0, 240, 240)\n"
"    );\n"
"    padding-bottom: 1px;\n"
"    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.15);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #e0e0e0, stop:1 #f0f0f0\n"
"    );\n"
"    color: #999;\n"
"    border-color: #ccc;\n"
"    box-shadow: none;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.button_TrainAndDiet)

        self.button_history = QToolButton(self.frame_3)
        self.button_history.setObjectName(u"button_history")
        sizePolicy9.setHeightForWidth(self.button_history.sizePolicy().hasHeightForWidth())
        self.button_history.setSizePolicy(sizePolicy9)
        icon17 = QIcon()
        icon17.addFile(u":/icons/icon/os-icon-history.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon17.addFile(u":/icons/icon/os-icon-history.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_history.setIcon(icon17)
        self.button_history.setCheckable(True)
        self.button_history.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_history)

        self.button_user = QToolButton(self.frame_3)
        self.button_user.setObjectName(u"button_user")
        sizePolicy9.setHeightForWidth(self.button_user.sizePolicy().hasHeightForWidth())
        self.button_user.setSizePolicy(sizePolicy9)
        icon18 = QIcon()
        icon18.addFile(u":/icons/icon/user-circle-single--circle-geometric-human-person-.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon18.addFile(u":/icons/icon/user-circle-single--circle-geometric-human-person-.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_user.setIcon(icon18)
        self.button_user.setCheckable(True)
        self.button_user.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_user)


        self.verticalLayout.addWidget(self.frame_3)


        self.verticalLayout_9.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_friend.setText(QCoreApplication.translate("MainWindow", u"friend", None))
        self.pushButton.setText("")
        self.label_train_diet_record.setText(QCoreApplication.translate("MainWindow", u" Diet Record", None))
        self.label_train_already_eaten.setText(QCoreApplication.translate("MainWindow", u"Already eaten 0/-- maximum calories", None))
        self.label_train_protein.setText(QCoreApplication.translate("MainWindow", u"Pro(g)\n"
"0\n"
"0% ", None))
        self.label_train_carbohydrate.setText(QCoreApplication.translate("MainWindow", u"Carbs(g)\n"
"0\n"
"0% ", None))
        self.label_train_fat.setText(QCoreApplication.translate("MainWindow", u"Fat(g)\n"
"0\n"
"0% ", None))
        self.label_train_water.setText(QCoreApplication.translate("MainWindow", u"H2O(ml)\n"
"0/0\n"
"0% ", None))
        self.button_train_breakfast.setText(QCoreApplication.translate("MainWindow", u"breakfast", None))
        self.button_train_lunch.setText(QCoreApplication.translate("MainWindow", u"lunch", None))
        self.button_train_dinner.setText(QCoreApplication.translate("MainWindow", u"dinner", None))
        self.button_train_extra_meal.setText(QCoreApplication.translate("MainWindow", u"extra-meal", None))
        self.button_train_drink.setText(QCoreApplication.translate("MainWindow", u"drink", None))
        self.button_train_weight.setText(QCoreApplication.translate("MainWindow", u"weight", None))
        self.button_train_official_plan.setText(QCoreApplication.translate("MainWindow", u"Official Plan", None))
        self.button_train_personal_plan.setText(QCoreApplication.translate("MainWindow", u"Personal Plan", None))
        self.button_train_plan1.setText(QCoreApplication.translate("MainWindow", u"plan1", None))
        self.button_train_plan2.setText(QCoreApplication.translate("MainWindow", u"plan2", None))
        self.button_train_plan3.setText(QCoreApplication.translate("MainWindow", u"plan3", None))
        self.button_train_plan4.setText(QCoreApplication.translate("MainWindow", u"plan4", None))
        self.button_sports_running_outside.setText(QCoreApplication.translate("MainWindow", u"Running-outside", None))
        self.button_sports_running_inside.setText(QCoreApplication.translate("MainWindow", u"Running-inside", None))
        self.button_sports_walk.setText(QCoreApplication.translate("MainWindow", u"Walk", None))
        self.button_sports_riding.setText(QCoreApplication.translate("MainWindow", u"Riding", None))
        self.button_sports_fitness.setText(QCoreApplication.translate("MainWindow", u"Fitness", None))
        self.button_sports_jump_rope.setText(QCoreApplication.translate("MainWindow", u"Jump-rope", None))
        self.button_sports_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.button_history_history.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.button_history_statistics.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.button_train.setText(QCoreApplication.translate("MainWindow", u"train", None))
        self.button_sports.setText(QCoreApplication.translate("MainWindow", u"sports", None))
        self.button_TrainAndDiet.setText(QCoreApplication.translate("MainWindow", u"T/D", None))
        self.button_history.setText(QCoreApplication.translate("MainWindow", u"history", None))
        self.button_user.setText(QCoreApplication.translate("MainWindow", u"user", None))
    # retranslateUi

