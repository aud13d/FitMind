# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FitMind_Client_Login.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QStackedWidget, QVBoxLayout,
    QWidget)

from ..res_rc import *

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(362, 666)
        LoginWindow.setMinimumSize(QSize(300, 666))
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_10 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
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
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer_2 = QSpacerItem(228, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.button_exit = QPushButton(self.frame_7)
        self.button_exit.setObjectName(u"button_exit")
        self.button_exit.setMinimumSize(QSize(0, 0))
        self.button_exit.setStyleSheet(u"QPushButton {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\"; \n"
"    border: 1px solid #ccc; /* \u7ec6\u8fb9\u6846 */\n"
"    border-radius: 6px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: white; /* \u7eaf\u767d\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"	border:none;\n"
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
        icon = QIcon()
        icon.addFile(u":/icons/icon/delete-1--remove-add-button-buttons-delete-cross-x.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_exit.setIcon(icon)
        self.button_exit.setIconSize(QSize(16, 16))

        self.horizontalLayout_6.addWidget(self.button_exit)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 25pt \"\u534e\u6587\u96b6\u4e66\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)


        self.verticalLayout_9.addWidget(self.frame_7)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(261, 461))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(5)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.frame_5)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy2)
        self.stackedWidget_2.setStyleSheet(u"QPushButton {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\"; \n"
"    border: 1px solid #ccc; /* \u7ec6\u8fb9\u6846 */\n"
"    border-radius: 6px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: black; /* \u7eaf\u9ed1\u80cc\u666f */\n"
"    color: white; /* \u767d\u8272\u6587\u5b57 */\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(15,15,15); /* \u6d45\u7070\u8272\u60ac\u6d6e\u6548\u679c */\n"
"    padding-bottom: 2px; /* \u8f7b\u5fae\u4e0b\u79fb\uff0c\u589e\u52a0\u6309\u538b\u611f */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(125,125,125); /* \u66f4\u6df1\u7684\u7070\u8272\uff0c\u6309\u4e0b\u6548\u679c */\n"
"    padding-bottom: 1px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #f8f8f8;\n"
"    color: gray;\n"
"    border-color: #ddd;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border: none; /* \u79fb\u9664\u6240\u6709\u8fb9\u6846 */\n"
"    border-bottom: 2px solid #5c9ef5; /* \u521d"
                        "\u59cb\u5e95\u90e8\u989c\u8272 */\n"
"    background-color: rgba(255, 255, 255, 0.3); /* \u534a\u900f\u660e\u80cc\u666f */\n"
"    padding: 5px 8px; /* \u9002\u5f53\u7684\u5185\u8fb9\u8ddd */\n"
"    color: #999999; /* \u5f85\u673a\u72b6\u6001\u5b57\u4f53\u989c\u8272\uff1a\u6d45\u7070\u8272 */\n"
"    selection-background-color: #a8d8ff; /* \u9009\u4e2d\u6587\u5b57\u7684\u80cc\u666f */\n"
"    transition: border-bottom 0.3s ease-in-out, color 0.3s ease-in-out; /* \u6dfb\u52a0\u989c\u8272\u6e10\u53d8 */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-bottom: 2px solid #3b7fd4; /* \u60ac\u6d6e\u65f6\u5e95\u90e8\u989c\u8272\u53d8\u6df1 */\n"
"    background-color: rgba(255, 255, 255, 0.5); /* \u63d0\u9ad8\u900f\u660e\u5ea6 */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-bottom: 2px solid #ff6600; /* \u805a\u7126\u65f6\u53d8\u6210\u6a59\u8272 */\n"
"    background-color: rgba(255, 255, 255, 0.7); /* \u805a\u7126\u65f6\u66f4\u52a0\u6e05\u6670 */\n"
"    color: black; /* \u8f93\u5165\u65f6\u5b57\u4f53\u989c\u8272"
                        "\u53d8\u9ed1 */\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.verticalLayout_5 = QVBoxLayout(self.page_login)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.line_login_username = QLineEdit(self.page_login)
        self.line_login_username.setObjectName(u"line_login_username")
        self.line_login_username.setMinimumSize(QSize(0, 30))

        self.verticalLayout_5.addWidget(self.line_login_username)

        self.line_login_password = QLineEdit(self.page_login)
        self.line_login_password.setObjectName(u"line_login_password")
        self.line_login_password.setMinimumSize(QSize(0, 30))
        self.line_login_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_5.addWidget(self.line_login_password)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.button_retrieve = QPushButton(self.page_login)
        self.button_retrieve.setObjectName(u"button_retrieve")
        self.button_retrieve.setMinimumSize(QSize(16, 16))
        self.button_retrieve.setStyleSheet(u"QPushButton {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\"; \n"
"    border: 1px solid #ccc; /* \u7ec6\u8fb9\u6846 */\n"
"    border-radius: 6px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: white; /* \u7eaf\u767d\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"	border:none;\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/question-mark.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_retrieve.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.button_retrieve)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.button_login_confirm = QPushButton(self.page_login)
        self.button_login_confirm.setObjectName(u"button_login_confirm")
        self.button_login_confirm.setMinimumSize(QSize(60, 30))

        self.verticalLayout_5.addWidget(self.button_login_confirm)

        self.stackedWidget_2.addWidget(self.page_login)
        self.page_register = QWidget()
        self.page_register.setObjectName(u"page_register")
        self.verticalLayout_6 = QVBoxLayout(self.page_register)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 9, 9, 6)
        self.line_register_email = QLineEdit(self.page_register)
        self.line_register_email.setObjectName(u"line_register_email")
        self.line_register_email.setMinimumSize(QSize(0, 30))

        self.verticalLayout_6.addWidget(self.line_register_email)

        self.line_register_username = QLineEdit(self.page_register)
        self.line_register_username.setObjectName(u"line_register_username")
        self.line_register_username.setMinimumSize(QSize(0, 30))

        self.verticalLayout_6.addWidget(self.line_register_username)

        self.line_register_password = QLineEdit(self.page_register)
        self.line_register_password.setObjectName(u"line_register_password")
        self.line_register_password.setMinimumSize(QSize(0, 30))
        self.line_register_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_6.addWidget(self.line_register_password)

        self.line_register_okpassword = QLineEdit(self.page_register)
        self.line_register_okpassword.setObjectName(u"line_register_okpassword")
        self.line_register_okpassword.setMinimumSize(QSize(0, 30))
        self.line_register_okpassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_6.addWidget(self.line_register_okpassword)

        self.splitter = QSplitter(self.page_register)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.line_register_verification = QLineEdit(self.splitter)
        self.line_register_verification.setObjectName(u"line_register_verification")
        self.splitter.addWidget(self.line_register_verification)
        self.button_register_verificationGet = QPushButton(self.splitter)
        self.button_register_verificationGet.setObjectName(u"button_register_verificationGet")
        self.button_register_verificationGet.setMinimumSize(QSize(60, 25))
        self.splitter.addWidget(self.button_register_verificationGet)

        self.verticalLayout_6.addWidget(self.splitter)

        self.button_register_confirm = QPushButton(self.page_register)
        self.button_register_confirm.setObjectName(u"button_register_confirm")
        self.button_register_confirm.setMinimumSize(QSize(60, 30))

        self.verticalLayout_6.addWidget(self.button_register_confirm)

        self.stackedWidget_2.addWidget(self.page_register)
        self.page_retrievePassword = QWidget()
        self.page_retrievePassword.setObjectName(u"page_retrievePassword")
        self.verticalLayout_7 = QVBoxLayout(self.page_retrievePassword)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.line_retrievePassword_email = QLineEdit(self.page_retrievePassword)
        self.line_retrievePassword_email.setObjectName(u"line_retrievePassword_email")
        self.line_retrievePassword_email.setMinimumSize(QSize(0, 30))

        self.verticalLayout_7.addWidget(self.line_retrievePassword_email)

        self.splitter_2 = QSplitter(self.page_retrievePassword)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.line_retrievePassword_verification = QLineEdit(self.splitter_2)
        self.line_retrievePassword_verification.setObjectName(u"line_retrievePassword_verification")
        self.line_retrievePassword_verification.setMinimumSize(QSize(0, 30))
        self.splitter_2.addWidget(self.line_retrievePassword_verification)
        self.button_retrievePassword_verificationGet = QPushButton(self.splitter_2)
        self.button_retrievePassword_verificationGet.setObjectName(u"button_retrievePassword_verificationGet")
        self.button_retrievePassword_verificationGet.setMinimumSize(QSize(60, 25))
        self.splitter_2.addWidget(self.button_retrievePassword_verificationGet)

        self.verticalLayout_7.addWidget(self.splitter_2)

        self.line_retrievePassword_password = QLineEdit(self.page_retrievePassword)
        self.line_retrievePassword_password.setObjectName(u"line_retrievePassword_password")
        self.line_retrievePassword_password.setMinimumSize(QSize(0, 30))
        self.line_retrievePassword_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_7.addWidget(self.line_retrievePassword_password)

        self.line_retrievePassword_okpassword = QLineEdit(self.page_retrievePassword)
        self.line_retrievePassword_okpassword.setObjectName(u"line_retrievePassword_okpassword")
        self.line_retrievePassword_okpassword.setMinimumSize(QSize(0, 30))
        self.line_retrievePassword_okpassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_7.addWidget(self.line_retrievePassword_okpassword)

        self.button_retrievePassword_confirm = QPushButton(self.page_retrievePassword)
        self.button_retrievePassword_confirm.setObjectName(u"button_retrievePassword_confirm")
        self.button_retrievePassword_confirm.setMinimumSize(QSize(0, 30))

        self.verticalLayout_7.addWidget(self.button_retrievePassword_confirm)

        self.stackedWidget_2.addWidget(self.page_retrievePassword)

        self.verticalLayout_4.addWidget(self.stackedWidget_2)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy3)
        self.frame_6.setStyleSheet(u"QPushButton {\n"
"    font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\"; \n"
"    border: 1px solid #ccc; /* \u7ec6\u8fb9\u6846 */\n"
"    border-radius: 6px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"    background-color: white; /* \u7eaf\u767d\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"	border:none;\n"
"    min-width: 60px;\n"
"    min-height: 25px;\n"
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
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_login = QPushButton(self.frame_6)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/login-1--arrow-enter-frame-left-login-point-rectan.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_login.setIcon(icon2)

        self.horizontalLayout.addWidget(self.button_login)

        self.button_register = QPushButton(self.frame_6)
        self.button_register.setObjectName(u"button_register")
        self.button_register.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/user-add-plus--actions-add-close-geometric-human-p.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_register.setIcon(icon3)

        self.horizontalLayout.addWidget(self.button_register)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_4)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_login_tap = QWidget()
        self.page_login_tap.setObjectName(u"page_login_tap")
        self.horizontalLayout_3 = QHBoxLayout(self.page_login_tap)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_login_error = QLabel(self.page_login_tap)
        self.label_login_error.setObjectName(u"label_login_error")

        self.horizontalLayout_3.addWidget(self.label_login_error)

        self.stackedWidget.addWidget(self.page_login_tap)
        self.page_register_tap = QWidget()
        self.page_register_tap.setObjectName(u"page_register_tap")
        self.horizontalLayout_4 = QHBoxLayout(self.page_register_tap)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_register_error = QLabel(self.page_register_tap)
        self.label_register_error.setObjectName(u"label_register_error")

        self.horizontalLayout_4.addWidget(self.label_register_error)

        self.stackedWidget.addWidget(self.page_register_tap)
        self.page_retrievePassword_tap = QWidget()
        self.page_retrievePassword_tap.setObjectName(u"page_retrievePassword_tap")
        self.horizontalLayout_5 = QHBoxLayout(self.page_retrievePassword_tap)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_retrievePassword_error = QLabel(self.page_retrievePassword_tap)
        self.label_retrievePassword_error.setObjectName(u"label_retrievePassword_error")

        self.horizontalLayout_5.addWidget(self.label_retrievePassword_error)

        self.stackedWidget.addWidget(self.page_retrievePassword_tap)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_4)


        self.verticalLayout_9.addWidget(self.frame_2)


        self.verticalLayout_10.addWidget(self.frame)

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        self.button_exit.clicked.connect(LoginWindow.close)

        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.button_exit.setText("")
        self.label.setText(QCoreApplication.translate("LoginWindow", u"Welcom To FitMind!", None))
        self.line_login_username.setInputMask("")
        self.line_login_username.setText("")
        self.line_login_username.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Please enter username...", None))
        self.line_login_password.setText("")
        self.line_login_password.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Please enter password...", None))
        self.button_retrieve.setText("")
        self.button_login_confirm.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.line_register_email.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Please enter QQ email...", None))
        self.line_register_username.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Please enter username...", None))
        self.line_register_password.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Please enter password...", None))
        self.line_register_okpassword.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Please confirm password...", None))
        self.line_register_verification.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Verification code...", None))
        self.button_register_verificationGet.setText(QCoreApplication.translate("LoginWindow", u"Get", None))
        self.button_register_confirm.setText(QCoreApplication.translate("LoginWindow", u"Register", None))
        self.line_retrievePassword_email.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Please enter QQ email...", None))
        self.line_retrievePassword_verification.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Verification code...", None))
        self.button_retrievePassword_verificationGet.setText(QCoreApplication.translate("LoginWindow", u"Get", None))
        self.line_retrievePassword_password.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Please enter password...", None))
        self.line_retrievePassword_okpassword.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Please confirm password...", None))
        self.button_retrievePassword_confirm.setText(QCoreApplication.translate("LoginWindow", u"Retrieve", None))
        self.button_login.setText("")
        self.button_register.setText("")
        self.label_login_error.setText("")
        self.label_register_error.setText("")
        self.label_retrievePassword_error.setText("")
    # retranslateUi

