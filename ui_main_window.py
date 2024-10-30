# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'ui_main_window.ui'
##
# Created by: Qt User Interface Compiler version 6.8.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
                               QLabel, QLineEdit, QMainWindow, QProgressBar,
                               QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
                               QVBoxLayout, QWidget)
import resources_file_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1179, 604)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(91, 112, 101);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ledtMenu_closed = QWidget(self.centralwidget)
        self.ledtMenu_closed.setObjectName(u"ledtMenu_closed")
        self.ledtMenu_closed.setStyleSheet(u"border: 1px solid rgb(48, 64, 64);\n"
                                           "color: rgb(48, 64, 64);\n"
                                           "border-radius: 5px;\n"
                                           "padding-top: 5px;\n"
                                           "padding-bottom:5 px;\n"
                                           "padding-left:5 px;\n"
                                           "padding-right:5px;")
        self.verticalLayout_22 = QVBoxLayout(self.ledtMenu_closed)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.widget_9 = QWidget(self.ledtMenu_closed)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_21 = QVBoxLayout(self.widget_9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.menuBtn_2 = QPushButton(self.widget_9)
        self.menuBtn_2.setObjectName(u"menuBtn_2")
        icon = QIcon()
        icon.addFile(u":/icons_png/C:/Users/Morpex/Desktop/24-Modern GUI exe/main/Qss/icons/fefefe/feather/menu.png",
                     QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn_2.setIcon(icon)

        self.verticalLayout_21.addWidget(self.menuBtn_2)

        self.verticalLayout_22.addWidget(self.widget_9)

        self.widget_8 = QWidget(self.ledtMenu_closed)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_20 = QVBoxLayout(self.widget_8)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.pushButton_13 = QPushButton(self.widget_8)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                         "font: 700 9pt \"Segoe UI\";")
        icon1 = QIcon()
        icon1.addFile(u":/icons_png/C:/Users/Morpex/Desktop/24-Modern GUI exe/main/Qss/icons/fefefe/feather/home.png",
                      QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_13.setIcon(icon1)

        self.verticalLayout_20.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.widget_8)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                         "font: 700 9pt \"Segoe UI\";")
        icon2 = QIcon()
        icon2.addFile(u":/icons_png/C:/Users/Morpex/Desktop/24-Modern GUI exe/main/Qss/icons/fefefe/feather/list.png",
                      QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_14.setIcon(icon2)

        self.verticalLayout_20.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.widget_8)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                         "font: 700 9pt \"Segoe UI\";")
        icon3 = QIcon()
        icon3.addFile(u":/icons_png/C:/Users/Morpex/Desktop/24-Modern GUI exe/main/Qss/icons/fefefe/feather/printer.png",
                      QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_15.setIcon(icon3)

        self.verticalLayout_20.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.widget_8)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                         "font: 700 9pt \"Segoe UI\";")
        icon4 = QIcon()
        icon4.addFile(u":/icons_png/C:/Users/Morpex/Desktop/24-Modern GUI exe/main/Qss/icons/fefefe/feather/pie-chart.png",
                      QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_16.setIcon(icon4)

        self.verticalLayout_20.addWidget(self.pushButton_16)

        self.verticalLayout_22.addWidget(self.widget_8)

        self.verticalSpacer_4 = QSpacerItem(
            20, 239, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_4)

        self.widget_7 = QWidget(self.ledtMenu_closed)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_19 = QVBoxLayout(self.widget_7)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.pushButton_9 = QPushButton(self.widget_7)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                        "font: 700 9pt \"Segoe UI\";")
        icon5 = QIcon()
        icon5.addFile(u":/icons_png/C:/Users/Morpex/Desktop/24-Modern GUI exe/main/Qss/icons/fefefe/feather/settings.png",
                      QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_9.setIcon(icon5)
        self.pushButton_9.setCheckable(True)

        self.verticalLayout_19.addWidget(self.pushButton_9)

        self.pushButton_11 = QPushButton(self.widget_7)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                         "font: 700 9pt \"Segoe UI\";")
        icon6 = QIcon()
        icon6.addFile(u":/icons_png/C:/Users/Morpex/Desktop/24-Modern GUI exe/main/Qss/icons/fefefe/feather/info.png",
                      QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon6)

        self.verticalLayout_19.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.widget_7)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                         "font: 700 9pt \"Segoe UI\";")
        icon7 = QIcon()
        icon7.addFile(u":/icons_png/C:/Users/Morpex/Desktop/24-Modern GUI exe/main/Qss/icons/fefefe/feather/help-circle.png",
                      QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_12.setIcon(icon7)

        self.verticalLayout_19.addWidget(self.pushButton_12)

        self.verticalLayout_22.addWidget(self.widget_7)

        self.horizontalLayout.addWidget(self.ledtMenu_closed)

        self.leftMenu = QWidget(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setStyleSheet(u"border: 1px solid rgb(48, 64, 64);\n"
                                    "color: rgb(48, 64, 64);\n"
                                    "border-radius: 5px;\n"
                                    "padding-top: 5px;\n"
                                    "padding-bottom:5 px;")
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.menuBtn = QPushButton(self.widget)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setEnabled(True)
        self.menuBtn.setStyleSheet(u"padding-top: 5px;\n"
                                   "padding-bottom:5 px;")
        self.menuBtn.setIcon(icon)

        self.verticalLayout_2.addWidget(self.menuBtn)

        self.verticalLayout.addWidget(self.widget)

        self.widget_3 = QWidget(self.leftMenu)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                      "font: 700 9pt \"Segoe UI\";\n"
                                      "padding-top: 5px;\n"
                                      "padding-bottom:5 px;")
        self.pushButton.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                        "font: 700 9pt \"Segoe UI\";\n"
                                        "padding-top: 5px;\n"
                                        "padding-bottom:5 px;")
        self.pushButton_2.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                        "font: 700 9pt \"Segoe UI\";\n"
                                        "padding-top: 5px;\n"
                                        "padding-bottom:5 px;")
        self.pushButton_3.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                        "font: 700 9pt \"Segoe UI\";\n"
                                        "padding-top: 5px;\n"
                                        "padding-bottom:5 px;")
        self.pushButton_4.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.verticalLayout.addWidget(self.widget_3)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_2 = QWidget(self.leftMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_5 = QPushButton(self.widget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                        "font: 700 9pt \"Segoe UI\";\n"
                                        "padding-top: 5px;\n"
                                        "padding-bottom:5 px;")
        self.pushButton_5.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                        "font: 700 9pt \"Segoe UI\";\n"
                                        "padding-top: 5px;\n"
                                        "padding-bottom:5 px;")
        self.pushButton_6.setIcon(icon6)

        self.verticalLayout_4.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.widget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                        "font: 700 9pt \"Segoe UI\";\n"
                                        "padding-top: 5px;\n"
                                        "padding-bottom:5 px;")
        self.pushButton_7.setIcon(icon7)

        self.verticalLayout_4.addWidget(self.pushButton_7)

        self.verticalLayout.addWidget(self.widget_2)

        self.horizontalLayout.addWidget(self.leftMenu)

        self.centerMenu = QWidget(self.centralwidget)
        self.centerMenu.setObjectName(u"centerMenu")
        self.centerMenu.setMaximumSize(QSize(200, 16777215))
        self.centerMenu.setStyleSheet(u"border: 1px solid rgb(48, 64, 64);\n"
                                      "color: rgb(48, 64, 64);\n"
                                      "border-radius: 5px;\n"
                                      "")
        self.verticalLayout_5 = QVBoxLayout(self.centerMenu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_4 = QWidget(self.centerMenu)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"border-color: rgb(48, 64, 64);")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"padding-top: 5px;\n"
                                 "padding-bottom:5 px;")

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton_8 = QPushButton(self.widget_4)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"padding-top: 5px;\n"
                                        "padding-bottom:5 px;")
        icon8 = QIcon()
        icon8.addFile(u":/icons_png/C:/Users/Morpex/Desktop/24-Modern GUI exe/main/Qss/icons/fefefe/feather/x-circle.png",
                      QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.pushButton_8)

        self.verticalLayout_5.addWidget(self.widget_4)

        self.stackedWidget = QStackedWidget(self.centerMenu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.setthingsPage = QWidget()
        self.setthingsPage.setObjectName(u"setthingsPage")
        self.setthingsPage.setStyleSheet(u"border:None;\n"
                                         "")
        self.verticalLayout_6 = QVBoxLayout(self.setthingsPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.widget_5 = QWidget(self.setthingsPage)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 0))
        self.verticalLayout_7 = QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.frame = QFrame(self.widget_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.verticalLayout_7.addWidget(self.frame)

        self.verticalLayout_6.addWidget(
            self.widget_5, 0, Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.setthingsPage)
        self.informationPage = QWidget()
        self.informationPage.setObjectName(u"informationPage")
        self.informationPage.setStyleSheet(u"border:None;\n"
                                           "")
        self.verticalLayout_8 = QVBoxLayout(self.informationPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.informationPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(
            self.label_4, 0, Qt.AlignmentFlag.AlignVCenter)

        self.stackedWidget.addWidget(self.informationPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.helpPage.setStyleSheet(u"border:None;")
        self.verticalLayout_9 = QVBoxLayout(self.helpPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.helpPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(
            self.label_5, 0, Qt.AlignmentFlag.AlignVCenter)

        self.stackedWidget.addWidget(self.helpPage)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.horizontalLayout.addWidget(self.centerMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.mainBody.setStyleSheet(u"border: 1px solid rgb(48, 64, 64);\n"
                                    "color: rgb(48, 64, 64);\n"
                                    "border-radius: 5px;\n"
                                    "padding-top: 5px;\n"
                                    "padding-bottom:5 px;")
        self.verticalLayout_10 = QVBoxLayout(self.mainBody)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.header = QWidget(self.mainBody)
        self.header.setObjectName(u"header")
        self.horizontalLayout_7 = QHBoxLayout(self.header)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 5, -1, 5)
        self.titleTxt = QLabel(self.header)
        self.titleTxt.setObjectName(u"titleTxt")

        self.horizontalLayout_7.addWidget(self.titleTxt)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, -1, 5)
        self.notificationBtn = QPushButton(self.frame_3)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons_png/C:/Users/Morpex/Desktop/24-Modern GUI exe/main/Qss/icons/fefefe/feather/bell.png",
                      QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notificationBtn.setIcon(icon9)

        self.horizontalLayout_6.addWidget(self.notificationBtn)

        self.moreBtn = QPushButton(self.frame_3)
        self.moreBtn.setObjectName(u"moreBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons_png/C:/Users/Morpex/Desktop/24-Modern GUI exe/main/Qss/icons/fefefe/feather/more-horizontal.png",
                       QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.moreBtn.setIcon(icon10)

        self.horizontalLayout_6.addWidget(self.moreBtn)

        self.profileBtn = QPushButton(self.frame_3)
        self.profileBtn.setObjectName(u"profileBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons_png/C:/Users/Morpex/Desktop/24-Modern GUI exe/main/Qss/icons/fefefe/feather/user.png",
                       QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profileBtn.setIcon(icon11)

        self.horizontalLayout_6.addWidget(self.profileBtn)

        self.horizontalLayout_7.addWidget(self.frame_3)

        self.searchInpCont = QFrame(self.header)
        self.searchInpCont.setObjectName(u"searchInpCont")
        self.searchInpCont.setFrameShape(QFrame.Shape.StyledPanel)
        self.searchInpCont.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.searchInpCont)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.label_9 = QLabel(self.searchInpCont)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(16)
        sizePolicy1.setVerticalStretch(16)
        sizePolicy1.setHeightForWidth(
            self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMinimumSize(QSize(10, 20))
        self.label_9.setMaximumSize(QSize(16, 50))
        self.label_9.setSizeIncrement(QSize(16, 16))
        self.label_9.setBaseSize(QSize(16, 16))
        self.label_9.setStyleSheet(u"")
        self.label_9.setPixmap(QPixmap(
            u":/icons_png/C:/Users/Morpex/Desktop/24-Modern GUI exe/main/Qss/icons/fefefe/feather/search.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignLeading |
                                  Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.searchInp = QLineEdit(self.searchInpCont)
        self.searchInp.setObjectName(u"searchInp")
        self.searchInp.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_8.addWidget(self.searchInp)

        self.searchBtn = QPushButton(self.searchInpCont)
        self.searchBtn.setObjectName(u"searchBtn")

        self.horizontalLayout_8.addWidget(self.searchBtn)

        self.horizontalLayout_7.addWidget(self.searchInpCont)

        self.frame_4 = QFrame(self.header)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 0, -1, 5)
        self.minimizeBtn = QPushButton(self.frame_4)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon12 = QIcon()
        icon12.addFile(u":/icons_png/C:/Users/Morpex/Desktop/24-Modern GUI exe/main/Qss/icons/fefefe/feather/window_minimize.png",
                       QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeBtn.setIcon(icon12)

        self.horizontalLayout_9.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_4)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icons_png/C:/Users/Morpex/Desktop/24-Modern GUI exe/main/Qss/icons/fefefe/feather/square.png",
                       QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restoreBtn.setIcon(icon13)

        self.horizontalLayout_9.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_4)
        self.closeBtn.setObjectName(u"closeBtn")
        icon14 = QIcon()
        icon14.addFile(u":/icons_png/C:/Users/Morpex/Desktop/24-Modern GUI exe/main/Qss/icons/fefefe/feather/window_close.png",
                       QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn.setIcon(icon14)

        self.horizontalLayout_9.addWidget(self.closeBtn)

        self.horizontalLayout_7.addWidget(
            self.frame_4, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_10.addWidget(
            self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.mainContents = QWidget(self.mainBody)
        self.mainContents.setObjectName(u"mainContents")
        sizePolicy.setHeightForWidth(
            self.mainContents.sizePolicy().hasHeightForWidth())
        self.mainContents.setSizePolicy(sizePolicy)
        self.horizontalLayout_10 = QHBoxLayout(self.mainContents)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.mainPagesCont = QWidget(self.mainContents)
        self.mainPagesCont.setObjectName(u"mainPagesCont")
        self.mainPagesCont.setMinimumSize(QSize(600, 0))
        self.mainPagesCont.setMaximumSize(QSize(200000, 200000))
        self.verticalLayout_11 = QVBoxLayout(self.mainPagesCont)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget_2 = QStackedWidget(self.mainPagesCont)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(20, 20))
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_12 = QVBoxLayout(self.homePage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.stackedWidget_2.addWidget(self.homePage)
        self.dataAnalysisPage = QWidget()
        self.dataAnalysisPage.setObjectName(u"dataAnalysisPage")
        self.verticalLayout_13 = QVBoxLayout(self.dataAnalysisPage)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_10 = QLabel(self.dataAnalysisPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_10)

        self.stackedWidget_2.addWidget(self.dataAnalysisPage)
        self.reportsPage = QWidget()
        self.reportsPage.setObjectName(u"reportsPage")
        self.horizontalLayout_11 = QHBoxLayout(self.reportsPage)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.reportsPage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_11)

        self.stackedWidget_2.addWidget(self.reportsPage)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_14 = QVBoxLayout(self.page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_12 = QLabel(self.page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_12)

        self.stackedWidget_2.addWidget(self.page)

        self.verticalLayout_11.addWidget(self.stackedWidget_2)

        self.horizontalLayout_10.addWidget(self.mainPagesCont)

        self.rightMenu = QWidget(self.mainContents)
        self.rightMenu.setObjectName(u"rightMenu")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.rightMenu.sizePolicy().hasHeightForWidth())
        self.rightMenu.setSizePolicy(sizePolicy2)
        self.rightMenu.setMinimumSize(QSize(0, 0))
        self.rightMenu.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_15 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.widget_6 = QWidget(self.rightMenu)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_13 = QLabel(self.widget_6)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_12.addWidget(self.label_13)

        self.pushButton_10 = QPushButton(self.widget_6)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setIcon(icon8)

        self.horizontalLayout_12.addWidget(self.pushButton_10)

        self.verticalLayout_15.addWidget(self.widget_6)

        self.stackedWidget_3 = QStackedWidget(self.rightMenu)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.notificationsPage = QWidget()
        self.notificationsPage.setObjectName(u"notificationsPage")
        self.verticalLayout_16 = QVBoxLayout(self.notificationsPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_14 = QLabel(self.notificationsPage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_14)

        self.stackedWidget_3.addWidget(self.notificationsPage)
        self.morePage = QWidget()
        self.morePage.setObjectName(u"morePage")
        self.verticalLayout_17 = QVBoxLayout(self.morePage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_15 = QLabel(self.morePage)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_15)

        self.stackedWidget_3.addWidget(self.morePage)
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        self.verticalLayout_18 = QVBoxLayout(self.profilePage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_16 = QLabel(self.profilePage)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_16)

        self.stackedWidget_3.addWidget(self.profilePage)

        self.verticalLayout_15.addWidget(self.stackedWidget_3)

        self.horizontalLayout_10.addWidget(self.rightMenu)

        self.verticalLayout_10.addWidget(self.mainContents)

        self.footer = QWidget(self.mainBody)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_4 = QHBoxLayout(self.footer)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_6 = QLabel(self.footer)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.frame_2 = QFrame(self.footer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout_5.addWidget(self.progressBar)

        self.horizontalLayout_4.addWidget(self.frame_2)

        self.sizeGrip = QFrame(self.footer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(15, 15))
        self.sizeGrip.setMaximumSize(QSize(15, 15))
        self.sizeGrip.setFrameShape(QFrame.Shape.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(
            self.sizeGrip, 0, Qt.AlignmentFlag.AlignBottom)

        self.verticalLayout_10.addWidget(
            self.footer, 0, Qt.AlignmentFlag.AlignBottom)

        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menuBtn_2.clicked.connect(self.ledtMenu_closed.hide)
        self.menuBtn_2.clicked.connect(self.leftMenu.show)
        self.menuBtn.clicked.connect(self.leftMenu.hide)
        self.menuBtn.clicked.connect(self.ledtMenu_closed.show)

        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.menuBtn_2.setText("")
        self.pushButton_13.setText("")
        self.pushButton_14.setText("")
        self.pushButton_15.setText("")
        self.pushButton_16.setText("")
        self.pushButton_9.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.menuBtn.setText("")
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_2.setText(QCoreApplication.translate(
            "MainWindow", u"Data Analysis", None))
        self.pushButton_3.setText(
            QCoreApplication.translate("MainWindow", u"Reports", None))
        self.pushButton_4.setText(
            QCoreApplication.translate("MainWindow", u"Graphs", None))
        self.pushButton_5.setText(QCoreApplication.translate(
            "MainWindow", u"Settings", None))
        self.pushButton_6.setText(QCoreApplication.translate(
            "MainWindow", u"Information", None))
        self.pushButton_7.setText(
            QCoreApplication.translate("MainWindow", u"Help", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Center Menu", None))
        self.pushButton_8.setText("")
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"Setthings", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"Theme", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"Information", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"Help", None))
        self.titleTxt.setText(QCoreApplication.translate(
            "MainWindow", u"23-Moder Ui", None))
        self.notificationBtn.setText("")
        self.moreBtn.setText("")
        self.profileBtn.setText("")
        self.label_9.setText("")
        self.searchInp.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Search...", None))
        self.searchBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Ctrl+K", None))
        self.minimizeBtn.setText("")
        self.restoreBtn.setText("")
        self.closeBtn.setText("")
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"Data Analysis", None))
        self.label_11.setText(QCoreApplication.translate(
            "MainWindow", u"Reports Page", None))
        self.label_12.setText(QCoreApplication.translate(
            "MainWindow", u"Charts Page", None))
        self.label_13.setText(QCoreApplication.translate(
            "MainWindow", u"Right Menu", None))
        self.pushButton_10.setText("")
        self.label_14.setText(QCoreApplication.translate(
            "MainWindow", u"Notifications", None))
        self.label_15.setText(QCoreApplication.translate(
            "MainWindow", u"More", None))
        self.label_16.setText(QCoreApplication.translate(
            "MainWindow", u"Profile", None))
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"AlexMorpex", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"Theme Progress", None))
    # retranslateUi
