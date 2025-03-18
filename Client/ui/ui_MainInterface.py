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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSplitter, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)
from .res_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(373, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 40, 261, 531))
        self.frame.setMinimumSize(QSize(261, 531))
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_train = QWidget()
        self.page_train.setObjectName(u"page_train")
        self.verticalLayout_5 = QVBoxLayout(self.page_train)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 4, 6, 4)
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


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.frame_10 = QFrame(self.page_train)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_10)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_10)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(10)
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setStyleSheet(u"    QScrollArea {\n"
" 		background: transparent;  /* \u900f\u660e\u80cc\u666f */\n"
"        border: none;  /* \u53ef\u9009\uff1a\u53bb\u6389\u8fb9\u6846 */\n"
"    }\n"
"    \n"
"    /* \u5782\u76f4\u6eda\u52a8\u6761 */\n"
"    QScrollBar:vertical {\n"
"        background: #f0f0f0;  /* \u6eda\u52a8\u6761\u80cc\u666f */\n"
"        width: 8px;  /* \u6eda\u52a8\u6761\u5bbd\u5ea6 */\n"
"        border-radius: 4px;\n"
"    }\n"
"    \n"
"    QScrollBar::handle:vertical {\n"
"        background: #c0c0c0;  /* \u6ed1\u5757\u989c\u8272 */\n"
"        border-radius: 4px;\n"
"        min-height: 20px;  /* \u6700\u5c0f\u9ad8\u5ea6 */\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical:hover {\n"
"        background: #a0a0a0;  /* \u60ac\u505c\u989c\u8272 */\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical:pressed {\n"
"        background: #808080;  /* \u6309\u4e0b\u65f6\u7684\u989c\u8272 */\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical,\n"
"    QScrollBar::add-line:vertical {\n"
"        background: none;  /* \u53bb"
                        "\u6389\u4e0a\u4e0b\u6309\u94ae */\n"
"    }\n"
"")
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 257, 451))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
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
"")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(3)
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setStyleSheet(u"font: 700 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)

        self.verticalLayout_3.addWidget(self.label_2)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(8)
        sizePolicy5.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy5)
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
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(5)
        sizePolicy6.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy6)
        self.frame_7.setStyleSheet(u"font: 700 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.frame_7)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_2.setHandleWidth(0)
        self.button_official_plan = QToolButton(self.splitter_2)
        self.button_official_plan.setObjectName(u"button_official_plan")
        self.button_official_plan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        self.splitter_2.addWidget(self.button_official_plan)
        self.button_personal_plan = QToolButton(self.splitter_2)
        self.button_personal_plan.setObjectName(u"button_personal_plan")
        self.splitter_2.addWidget(self.button_personal_plan)

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
        sizePolicy5.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy5)
        self.frame_8.setStyleSheet(u"font: 290 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.splitter_3 = QSplitter(self.frame_8)
        self.splitter_3.setObjectName(u"splitter_3")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.splitter_3.sizePolicy().hasHeightForWidth())
        self.splitter_3.setSizePolicy(sizePolicy7)
        self.splitter_3.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_3.setHandleWidth(0)
        self.button_plan1 = QToolButton(self.splitter_3)
        self.button_plan1.setObjectName(u"button_plan1")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.button_plan1.sizePolicy().hasHeightForWidth())
        self.button_plan1.setSizePolicy(sizePolicy8)
        self.splitter_3.addWidget(self.button_plan1)
        self.button_plan2 = QToolButton(self.splitter_3)
        self.button_plan2.setObjectName(u"button_plan2")
        sizePolicy8.setHeightForWidth(self.button_plan2.sizePolicy().hasHeightForWidth())
        self.button_plan2.setSizePolicy(sizePolicy8)
        self.splitter_3.addWidget(self.button_plan2)
        self.button_plan3 = QToolButton(self.splitter_3)
        self.button_plan3.setObjectName(u"button_plan3")
        self.splitter_3.addWidget(self.button_plan3)
        self.button_plan4 = QToolButton(self.splitter_3)
        self.button_plan4.setObjectName(u"button_plan4")
        self.splitter_3.addWidget(self.button_plan4)

        self.verticalLayout_7.addWidget(self.splitter_3)

        self.stackedWidget_3 = QStackedWidget(self.frame_8)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
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


        self.verticalLayout_9.addWidget(self.frame_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.page_train)
        self.page_sports = QWidget()
        self.page_sports.setObjectName(u"page_sports")
        self.stackedWidget.addWidget(self.page_sports)
        self.page_history = QWidget()
        self.page_history.setObjectName(u"page_history")
        self.stackedWidget.addWidget(self.page_history)
        self.page_user = QWidget()
        self.page_user.setObjectName(u"page_user")
        self.stackedWidget.addWidget(self.page_user)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(1)
        sizePolicy9.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy9)
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
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/dongzuo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icons/icon/dongzuo.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_sports.setIcon(icon3)
        self.button_sports.setCheckable(True)
        self.button_sports.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_sports)

        self.button_history = QToolButton(self.frame_3)
        self.button_history.setObjectName(u"button_history")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/os-icon-history.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icons/icon/os-icon-history.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_history.setIcon(icon4)
        self.button_history.setCheckable(True)
        self.button_history.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_history)

        self.button_user = QToolButton(self.frame_3)
        self.button_user.setObjectName(u"button_user")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icon/user-circle-single--circle-geometric-human-person-.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/icons/icon/user-circle-single--circle-geometric-human-person-.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_user.setIcon(icon5)
        self.button_user.setCheckable(True)
        self.button_user.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_user)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_friend.setText(QCoreApplication.translate("MainWindow", u"friend", None))
        self.pushButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" Diet Record", None))
        self.button_official_plan.setText(QCoreApplication.translate("MainWindow", u"Official Plan", None))
        self.button_personal_plan.setText(QCoreApplication.translate("MainWindow", u"Personal Plan", None))
        self.button_plan1.setText(QCoreApplication.translate("MainWindow", u"plan1", None))
        self.button_plan2.setText(QCoreApplication.translate("MainWindow", u"plan2", None))
        self.button_plan3.setText(QCoreApplication.translate("MainWindow", u"plan3", None))
        self.button_plan4.setText(QCoreApplication.translate("MainWindow", u"plan4", None))
        self.button_train.setText(QCoreApplication.translate("MainWindow", u"train", None))
        self.button_sports.setText(QCoreApplication.translate("MainWindow", u"sports", None))
        self.button_history.setText(QCoreApplication.translate("MainWindow", u"history", None))
        self.button_user.setText(QCoreApplication.translate("MainWindow", u"user", None))
    # retranslateUi

