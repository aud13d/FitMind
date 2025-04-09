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
        MainWindow.resize(362, 701)
        MainWindow.setMinimumSize(QSize(300, 666))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_9 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
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
        self.horizontalLayout_3.setContentsMargins(-1, 4, 0, 0)
        self.horizontalSpacer = QSpacerItem(90, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.button_friend = QPushButton(self.page_train)
        self.button_friend.setObjectName(u"button_friend")
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

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.horizontalLayout_3.setStretch(0, 8)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.frame_10 = QFrame(self.page_train)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
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
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical {\n"
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
"    background: rgba(100, 100, 100, 0.8);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal,"
                        "\n"
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
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
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QSize(0, 200))
        self.frame_5.setStyleSheet(u"font: 700 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.label_2)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(8)
        sizePolicy3.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy3)
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_10.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QSize(0, 0))
        self.frame_7.setStyleSheet(u"font: 700 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
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
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_7.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.frame_7)
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

        self.stackedWidget_2 = QStackedWidget(self.frame_7)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_official_plan = QWidget()
        self.page_official_plan.setObjectName(u"page_official_plan")
        self.verticalLayout_8 = QVBoxLayout(self.page_official_plan)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 9, 0, 0)
        self.frame_8 = QFrame(self.page_official_plan)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy3.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy3)
        self.frame_8.setStyleSheet(u"font: 290 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.splitter_3 = QSplitter(self.frame_8)
        self.splitter_3.setObjectName(u"splitter_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.splitter_3.sizePolicy().hasHeightForWidth())
        self.splitter_3.setSizePolicy(sizePolicy4)
        self.splitter_3.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_3.setHandleWidth(0)
        self.button_train_plan1 = QToolButton(self.splitter_3)
        self.button_train_plan1.setObjectName(u"button_train_plan1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.button_train_plan1.sizePolicy().hasHeightForWidth())
        self.button_train_plan1.setSizePolicy(sizePolicy5)
        self.button_train_plan1.setCheckable(True)
        self.splitter_3.addWidget(self.button_train_plan1)
        self.button_train_plan2 = QToolButton(self.splitter_3)
        self.button_train_plan2.setObjectName(u"button_train_plan2")
        sizePolicy5.setHeightForWidth(self.button_train_plan2.sizePolicy().hasHeightForWidth())
        self.button_train_plan2.setSizePolicy(sizePolicy5)
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


        self.verticalLayout_10.addWidget(self.frame_7)


        self.horizontalLayout_6.addWidget(self.frame_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 9)
        self.stackedWidget.addWidget(self.page_train)
        self.page_sports = QWidget()
        self.page_sports.setObjectName(u"page_sports")
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
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy6)
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
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.button_history_history.sizePolicy().hasHeightForWidth())
        self.button_history_history.setSizePolicy(sizePolicy7)
        self.button_history_history.setMinimumSize(QSize(60, 60))
        self.button_history_history.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.button_history_history)

        self.button_history_statistics = QToolButton(self.frame_11)
        self.button_history_statistics.setObjectName(u"button_history_statistics")
        sizePolicy7.setHeightForWidth(self.button_history_statistics.sizePolicy().hasHeightForWidth())
        self.button_history_statistics.setSizePolicy(sizePolicy7)
        self.button_history_statistics.setMinimumSize(QSize(60, 60))
        self.button_history_statistics.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.button_history_statistics)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.page_history)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(10)
        sizePolicy8.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy8)
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
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_train = QToolButton(self.frame_3)
        self.button_train.setObjectName(u"button_train")
        sizePolicy7.setHeightForWidth(self.button_train.sizePolicy().hasHeightForWidth())
        self.button_train.setSizePolicy(sizePolicy7)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/xunlianjihua.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/icon/xunlianjihua.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_train.setIcon(icon2)
        self.button_train.setIconSize(QSize(16, 16))
        self.button_train.setCheckable(True)
        self.button_train.setChecked(False)
        self.button_train.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_train)

        self.button_sports = QToolButton(self.frame_3)
        self.button_sports.setObjectName(u"button_sports")
        sizePolicy7.setHeightForWidth(self.button_sports.sizePolicy().hasHeightForWidth())
        self.button_sports.setSizePolicy(sizePolicy7)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/dongzuo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icons/icon/dongzuo.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_sports.setIcon(icon3)
        self.button_sports.setCheckable(True)
        self.button_sports.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_sports)

        self.button_TrainAndDiet = QPushButton(self.frame_3)
        self.button_TrainAndDiet.setObjectName(u"button_TrainAndDiet")
        sizePolicy7.setHeightForWidth(self.button_TrainAndDiet.sizePolicy().hasHeightForWidth())
        self.button_TrainAndDiet.setSizePolicy(sizePolicy7)
        self.button_TrainAndDiet.setMinimumSize(QSize(62, 47))
        self.button_TrainAndDiet.setMaximumSize(QSize(16777215, 16777215))
        self.button_TrainAndDiet.setStyleSheet(u"QPushButton {\n"
"    font: 700 16pt \"\u5fae\u8f6f\u96c5\u9ed1\"; \n"
"    border: 1px solid #ccc; /* \u7ec6\u8fb9\u6846 */\n"
"    border-radius: 16px; /* \u66f4\u5706\u7684\u5706\u89d2\uff0c\u589e\u52a0\u8d28\u611f */\n"
"    \n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(56, 230, 148, 255), stop:1 rgba(255, 255, 255, 50));\n"
"    color: white; /* \u767d\u8272\u6587\u5b57\uff0c\u4f7f\u6587\u5b57\u4e0e\u80cc\u666f\u6709\u5bf9\u6bd4 */\n"
"    min-width: 60px;\n"
"    min-height: 45px;\n"
"    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.5); /* \u6dfb\u52a0\u8f7b\u5fae\u9634\u5f71 */\n"
"    outline: none; /* \u53bb\u9664\u9ed8\u8ba4\u8f6e\u5ed3\u7ebf */\n"
"    transition: all 0.3s ease; /* \u5e73\u6ed1\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* \u60ac\u6d6e\u65f6\u6e10\u53d8\u8272\u52a0\u6df1 */\n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(34, 192, 112, 255), stop:1 rgba(255, 255, 255, 70"
                        "));\n"
"    padding-bottom: 2px; /* \u8f7b\u5fae\u4e0b\u79fb\uff0c\u589e\u52a0\u6309\u538b\u611f */\n"
"    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.15); /* \u60ac\u6d6e\u65f6\u52a0\u6df1\u9634\u5f71 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* \u6309\u4e0b\u65f6\u6e10\u53d8\u8272\u66f4\u6df1 */\n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(23, 170, 83, 255), stop:1 rgba(255, 255, 255, 90));\n"
"    padding-bottom: 1px;\n"
"    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.2); /* \u6309\u4e0b\u65f6\u51cf\u5c0f\u9634\u5f71 */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: linear-gradient(to right, #cce5ff, #d4edda); /* \u7981\u7528\u65f6\u6d45\u8272\u6e10\u53d8 */\n"
"    color: gray;\n"
"    border-color: #ddd;\n"
"    box-shadow: none; /* \u7981\u7528\u65f6\u53bb\u9664\u9634\u5f71 */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.button_TrainAndDiet)

        self.button_history = QToolButton(self.frame_3)
        self.button_history.setObjectName(u"button_history")
        sizePolicy7.setHeightForWidth(self.button_history.sizePolicy().hasHeightForWidth())
        self.button_history.setSizePolicy(sizePolicy7)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/os-icon-history.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icons/icon/os-icon-history.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_history.setIcon(icon4)
        self.button_history.setCheckable(True)
        self.button_history.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_history)

        self.button_user = QToolButton(self.frame_3)
        self.button_user.setObjectName(u"button_user")
        sizePolicy7.setHeightForWidth(self.button_user.sizePolicy().hasHeightForWidth())
        self.button_user.setSizePolicy(sizePolicy7)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icon/user-circle-single--circle-geometric-human-person-.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/icons/icon/user-circle-single--circle-geometric-human-person-.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_user.setIcon(icon5)
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" Diet Record", None))
        self.button_train_official_plan.setText(QCoreApplication.translate("MainWindow", u"Official Plan", None))
        self.button_train_personal_plan.setText(QCoreApplication.translate("MainWindow", u"Personal Plan", None))
        self.button_train_plan1.setText(QCoreApplication.translate("MainWindow", u"plan1", None))
        self.button_train_plan2.setText(QCoreApplication.translate("MainWindow", u"plan2", None))
        self.button_train_plan3.setText(QCoreApplication.translate("MainWindow", u"plan3", None))
        self.button_train_plan4.setText(QCoreApplication.translate("MainWindow", u"plan4", None))
        self.button_history_history.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.button_history_statistics.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.button_train.setText(QCoreApplication.translate("MainWindow", u"train", None))
        self.button_sports.setText(QCoreApplication.translate("MainWindow", u"sports", None))
        self.button_TrainAndDiet.setText(QCoreApplication.translate("MainWindow", u"T/D", None))
        self.button_history.setText(QCoreApplication.translate("MainWindow", u"history", None))
        self.button_user.setText(QCoreApplication.translate("MainWindow", u"user", None))
    # retranslateUi

