# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FitMind_Client_AddAction.ui'
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
    QLabel, QLayout, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from ..res_rc import *

class Ui_Dialog_add_action(object):
    def setupUi(self, Dialog_add_action):
        if not Dialog_add_action.objectName():
            Dialog_add_action.setObjectName(u"Dialog_add_action")
        Dialog_add_action.resize(362, 700)
        Dialog_add_action.setMinimumSize(QSize(300, 666))
        self.horizontalLayout = QHBoxLayout(Dialog_add_action)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog_add_action)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame{\n"
"	background-color:white;\n"
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
"    border-color: #ddd;\n"
"}"
                        "\n"
"\n"
"\n"
"#label {\n"
"	font: 700 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, -1, 0, -1)
        self.button_back = QPushButton(self.frame)
        self.button_back.setObjectName(u"button_back")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_back.sizePolicy().hasHeightForWidth())
        self.button_back.setSizePolicy(sizePolicy)
        self.button_back.setMinimumSize(QSize(60, 45))
        self.button_back.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icon/delete-1--remove-add-button-buttons-delete-cross-x.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_back.setIcon(icon)
        self.button_back.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.button_back)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 7)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"	background-color:white;\n"
"	border-top-right-radius:20px;\n"
"	border-top-left-radius:20px;\n"
"	border-bottom-right-radius:20px;\n"
"	border-bottom-left-radius:20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font: 550 10pt \"\u5fae\u8f6f\u96c5\u9ed1\"; \n"
"    border-radius: 6px; /* \u8f7b\u5fae\u5706\u89d2 */\n"
"	background-color: none;\n"
"    color: black; /* \u9ed1\u8272\u6587\u5b57 */\n"
"	border:none;\n"
"	text-align: left;\n"
"}\n"
"\n"
"\n"
"QScrollArea {\n"
"	border:none;\n"
"	background-color: none;\n"
"	border-top-right-radius:15px;\n"
"	border-top-left-radius:15px;\n"
"	border-bottom-right-radius:15px;\n"
"	border-bottom-left-radius:15px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: none;\n"
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
"    background: rgba(100, "
                        "100, 100, 0.8);\n"
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
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(362, 646))
        self.scrollArea.setStyleSheet(u"QFrame{\n"
"	background-color:white;\n"
"	border-top-right-radius:15px;\n"
"	border-top-left-radius:15px;\n"
"	border-bottom-right-radius:15px;\n"
"	border-bottom-left-radius:15px;\n"
"}\n"
"\n"
"QWidget{\n"
"	border-top-right-radius:20px;\n"
"	border-top-left-radius:20px;\n"
"	border-bottom-right-radius:20px;\n"
"	border-bottom-left-radius:20px;\n"
"}")
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 362, 646))
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(9, 10, 217, 16))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font: 8pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    border-radius: 9px; /* \u5706\u89d2 */\n"
"    background-color: none; /* \u80cc\u666f\u989c\u8272 */\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"}\n"
"")
        self.frame_running_outside = QFrame(self.scrollAreaWidgetContents)
        self.frame_running_outside.setObjectName(u"frame_running_outside")
        self.frame_running_outside.setGeometry(QRect(9, 35, 350, 55))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_running_outside.sizePolicy().hasHeightForWidth())
        self.frame_running_outside.setSizePolicy(sizePolicy2)
        self.frame_running_outside.setMinimumSize(QSize(350, 55))
        self.frame_running_outside.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_running_outside.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_running_outside)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.label_running_outside_move = QLabel(self.frame_running_outside)
        self.label_running_outside_move.setObjectName(u"label_running_outside_move")
        self.label_running_outside_move.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.label_running_outside_move)

        self.button_running_outside = QPushButton(self.frame_running_outside)
        self.button_running_outside.setObjectName(u"button_running_outside")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.button_running_outside.sizePolicy().hasHeightForWidth())
        self.button_running_outside.setSizePolicy(sizePolicy3)
        self.button_running_outside.setMinimumSize(QSize(0, 0))
        self.button_running_outside.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_running_outside.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/benpao.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_running_outside.setIcon(icon1)
        self.button_running_outside.setIconSize(QSize(36, 36))

        self.horizontalLayout_4.addWidget(self.button_running_outside)

        self.label_running_outside_go = QLabel(self.frame_running_outside)
        self.label_running_outside_go.setObjectName(u"label_running_outside_go")

        self.horizontalLayout_4.addWidget(self.label_running_outside_go)

        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 10)
        self.horizontalLayout_4.setStretch(2, 2)
        self.frame_running_inside = QFrame(self.scrollAreaWidgetContents)
        self.frame_running_inside.setObjectName(u"frame_running_inside")
        self.frame_running_inside.setGeometry(QRect(10, 100, 350, 55))
        sizePolicy2.setHeightForWidth(self.frame_running_inside.sizePolicy().hasHeightForWidth())
        self.frame_running_inside.setSizePolicy(sizePolicy2)
        self.frame_running_inside.setMinimumSize(QSize(350, 55))
        self.frame_running_inside.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_running_inside.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_running_inside)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.label_running_inside_move = QLabel(self.frame_running_inside)
        self.label_running_inside_move.setObjectName(u"label_running_inside_move")
        self.label_running_inside_move.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.label_running_inside_move)

        self.button_running_inside = QPushButton(self.frame_running_inside)
        self.button_running_inside.setObjectName(u"button_running_inside")
        sizePolicy3.setHeightForWidth(self.button_running_inside.sizePolicy().hasHeightForWidth())
        self.button_running_inside.setSizePolicy(sizePolicy3)
        self.button_running_inside.setMinimumSize(QSize(0, 0))
        self.button_running_inside.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_running_inside.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/shineipaobu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_running_inside.setIcon(icon2)
        self.button_running_inside.setIconSize(QSize(36, 36))

        self.horizontalLayout_5.addWidget(self.button_running_inside)

        self.label_running_inside_go = QLabel(self.frame_running_inside)
        self.label_running_inside_go.setObjectName(u"label_running_inside_go")

        self.horizontalLayout_5.addWidget(self.label_running_inside_go)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 10)
        self.horizontalLayout_5.setStretch(2, 2)
        self.frame_walk = QFrame(self.scrollAreaWidgetContents)
        self.frame_walk.setObjectName(u"frame_walk")
        self.frame_walk.setGeometry(QRect(10, 170, 350, 55))
        sizePolicy2.setHeightForWidth(self.frame_walk.sizePolicy().hasHeightForWidth())
        self.frame_walk.setSizePolicy(sizePolicy2)
        self.frame_walk.setMinimumSize(QSize(350, 55))
        self.frame_walk.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_walk.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_walk)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.label_walk_move = QLabel(self.frame_walk)
        self.label_walk_move.setObjectName(u"label_walk_move")
        self.label_walk_move.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_6.addWidget(self.label_walk_move)

        self.button_walk = QPushButton(self.frame_walk)
        self.button_walk.setObjectName(u"button_walk")
        sizePolicy3.setHeightForWidth(self.button_walk.sizePolicy().hasHeightForWidth())
        self.button_walk.setSizePolicy(sizePolicy3)
        self.button_walk.setMinimumSize(QSize(0, 0))
        self.button_walk.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_walk.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/walk.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_walk.setIcon(icon3)
        self.button_walk.setIconSize(QSize(36, 36))

        self.horizontalLayout_6.addWidget(self.button_walk)

        self.label_walk_go = QLabel(self.frame_walk)
        self.label_walk_go.setObjectName(u"label_walk_go")

        self.horizontalLayout_6.addWidget(self.label_walk_go)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 10)
        self.horizontalLayout_6.setStretch(2, 2)
        self.frame_riding = QFrame(self.scrollAreaWidgetContents)
        self.frame_riding.setObjectName(u"frame_riding")
        self.frame_riding.setGeometry(QRect(10, 240, 350, 55))
        sizePolicy2.setHeightForWidth(self.frame_riding.sizePolicy().hasHeightForWidth())
        self.frame_riding.setSizePolicy(sizePolicy2)
        self.frame_riding.setMinimumSize(QSize(350, 55))
        self.frame_riding.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_riding.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_riding)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.label_riding_move = QLabel(self.frame_riding)
        self.label_riding_move.setObjectName(u"label_riding_move")
        self.label_riding_move.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_7.addWidget(self.label_riding_move)

        self.button_riding = QPushButton(self.frame_riding)
        self.button_riding.setObjectName(u"button_riding")
        sizePolicy3.setHeightForWidth(self.button_riding.sizePolicy().hasHeightForWidth())
        self.button_riding.setSizePolicy(sizePolicy3)
        self.button_riding.setMinimumSize(QSize(0, 0))
        self.button_riding.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_riding.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/\u9a91\u884c.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_riding.setIcon(icon4)
        self.button_riding.setIconSize(QSize(36, 36))

        self.horizontalLayout_7.addWidget(self.button_riding)

        self.label_riding_go = QLabel(self.frame_riding)
        self.label_riding_go.setObjectName(u"label_riding_go")

        self.horizontalLayout_7.addWidget(self.label_riding_go)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 10)
        self.horizontalLayout_7.setStretch(2, 2)
        self.frame_fitness = QFrame(self.scrollAreaWidgetContents)
        self.frame_fitness.setObjectName(u"frame_fitness")
        self.frame_fitness.setGeometry(QRect(10, 310, 351, 55))
        sizePolicy2.setHeightForWidth(self.frame_fitness.sizePolicy().hasHeightForWidth())
        self.frame_fitness.setSizePolicy(sizePolicy2)
        self.frame_fitness.setMinimumSize(QSize(350, 55))
        self.frame_fitness.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fitness.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_fitness)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.label_fitness_move = QLabel(self.frame_fitness)
        self.label_fitness_move.setObjectName(u"label_fitness_move")
        self.label_fitness_move.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_8.addWidget(self.label_fitness_move)

        self.button_fitness = QPushButton(self.frame_fitness)
        self.button_fitness.setObjectName(u"button_fitness")
        sizePolicy3.setHeightForWidth(self.button_fitness.sizePolicy().hasHeightForWidth())
        self.button_fitness.setSizePolicy(sizePolicy3)
        self.button_fitness.setMinimumSize(QSize(0, 0))
        self.button_fitness.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_fitness.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icon/ticao.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_fitness.setIcon(icon5)
        self.button_fitness.setIconSize(QSize(36, 36))

        self.horizontalLayout_8.addWidget(self.button_fitness)

        self.label_fitness_go = QLabel(self.frame_fitness)
        self.label_fitness_go.setObjectName(u"label_fitness_go")

        self.horizontalLayout_8.addWidget(self.label_fitness_go)

        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 10)
        self.horizontalLayout_8.setStretch(2, 2)
        self.frame_jump_rope = QFrame(self.scrollAreaWidgetContents)
        self.frame_jump_rope.setObjectName(u"frame_jump_rope")
        self.frame_jump_rope.setGeometry(QRect(10, 380, 350, 55))
        sizePolicy2.setHeightForWidth(self.frame_jump_rope.sizePolicy().hasHeightForWidth())
        self.frame_jump_rope.setSizePolicy(sizePolicy2)
        self.frame_jump_rope.setMinimumSize(QSize(350, 55))
        self.frame_jump_rope.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_jump_rope.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_jump_rope)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_jump_rope_move = QLabel(self.frame_jump_rope)
        self.label_jump_rope_move.setObjectName(u"label_jump_rope_move")
        self.label_jump_rope_move.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_9.addWidget(self.label_jump_rope_move)

        self.button_jump_rope = QPushButton(self.frame_jump_rope)
        self.button_jump_rope.setObjectName(u"button_jump_rope")
        sizePolicy3.setHeightForWidth(self.button_jump_rope.sizePolicy().hasHeightForWidth())
        self.button_jump_rope.setSizePolicy(sizePolicy3)
        self.button_jump_rope.setMinimumSize(QSize(0, 0))
        self.button_jump_rope.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_jump_rope.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icon/tiaosheng.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_jump_rope.setIcon(icon6)
        self.button_jump_rope.setIconSize(QSize(36, 36))

        self.horizontalLayout_9.addWidget(self.button_jump_rope)

        self.label_jump_rope_go = QLabel(self.frame_jump_rope)
        self.label_jump_rope_go.setObjectName(u"label_jump_rope_go")

        self.horizontalLayout_9.addWidget(self.label_jump_rope_go)

        self.horizontalLayout_9.setStretch(0, 2)
        self.horizontalLayout_9.setStretch(1, 10)
        self.horizontalLayout_9.setStretch(2, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 12)

        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog_add_action)
        self.button_back.clicked.connect(Dialog_add_action.close)

        QMetaObject.connectSlotsByName(Dialog_add_action)
    # setupUi

    def retranslateUi(self, Dialog_add_action):
        Dialog_add_action.setWindowTitle(QCoreApplication.translate("Dialog_add_action", u"Dialog", None))
        self.button_back.setText("")
        self.label.setText(QCoreApplication.translate("Dialog_add_action", u"All actions", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_add_action", u"Click to select the action you want to add", None))
        self.label_running_outside_move.setText("")
        self.button_running_outside.setText(QCoreApplication.translate("Dialog_add_action", u"Running-outside", None))
        self.label_running_outside_go.setText("")
        self.label_running_inside_move.setText("")
        self.button_running_inside.setText(QCoreApplication.translate("Dialog_add_action", u"Running-inside", None))
        self.label_running_inside_go.setText("")
        self.label_walk_move.setText("")
        self.button_walk.setText(QCoreApplication.translate("Dialog_add_action", u"Walk", None))
        self.label_walk_go.setText("")
        self.label_riding_move.setText("")
        self.button_riding.setText(QCoreApplication.translate("Dialog_add_action", u"Ridding", None))
        self.label_riding_go.setText("")
        self.label_fitness_move.setText("")
        self.button_fitness.setText(QCoreApplication.translate("Dialog_add_action", u"FitNess", None))
        self.label_fitness_go.setText("")
        self.label_jump_rope_move.setText("")
        self.button_jump_rope.setText(QCoreApplication.translate("Dialog_add_action", u"Jump-rope", None))
        self.label_jump_rope_go.setText("")
    # retranslateUi

