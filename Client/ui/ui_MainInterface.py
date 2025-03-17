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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QSizePolicy, QStackedWidget, QToolButton, QVBoxLayout,
    QWidget)
import res_rc

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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setStyleSheet(u"QToolButton {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\"; \n"
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
        icon = QIcon()
        icon.addFile(u":/icons/icon/xunlianjihua.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/icons/icon/xunlianjihua.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_train.setIcon(icon)
        self.button_train.setIconSize(QSize(16, 16))
        self.button_train.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_train)

        self.button_sports = QToolButton(self.frame_3)
        self.button_sports.setObjectName(u"button_sports")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/dongzuo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icons/icon/dongzuo.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_sports.setIcon(icon1)
        self.button_sports.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_sports)

        self.button_history = QToolButton(self.frame_3)
        self.button_history.setObjectName(u"button_history")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/os-icon-history.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/icon/os-icon-history.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_history.setIcon(icon2)
        self.button_history.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_history)

        self.button_user = QToolButton(self.frame_3)
        self.button_user.setObjectName(u"button_user")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/user-circle-single--circle-geometric-human-person-.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icons/icon/user-circle-single--circle-geometric-human-person-.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.button_user.setIcon(icon3)
        self.button_user.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_user)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_train.setText(QCoreApplication.translate("MainWindow", u"train", None))
        self.button_sports.setText(QCoreApplication.translate("MainWindow", u"sports", None))
        self.button_history.setText(QCoreApplication.translate("MainWindow", u"history", None))
        self.button_user.setText(QCoreApplication.translate("MainWindow", u"user", None))
    # retranslateUi

