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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
                               QWidget)
import resources_file


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1262, 733)
        MainWindow.setStyleSheet(u"background-color: rgb(91, 112, 101);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(1220, 0, 41, 20))
        font = QFont()
        font.setFamilies([u"Microsoft Yi Baiti"])
        font.setPointSize(14)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet(u"border:0px;")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.btn_exit.setIcon(icon)
        self.btn_exit.setIconSize(QSize(10, 10))
        self.btn_collapse = QPushButton(self.centralwidget)
        self.btn_collapse.setObjectName(u"btn_collapse")
        self.btn_collapse.setGeometry(QRect(1140, 0, 41, 20))
        font1 = QFont()
        font1.setFamilies([u"Myanmar Text"])
        font1.setPointSize(16)
        self.btn_collapse.setFont(font1)
        self.btn_collapse.setStyleSheet(u"border:0px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minimize.svg", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_collapse.setIcon(icon1)
        self.btn_collapse.setIconSize(QSize(12, 12))
        self.btn_maximize = QPushButton(self.centralwidget)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setGeometry(QRect(1180, 0, 41, 20))
        self.btn_maximize.setFont(font)
        self.btn_maximize.setStyleSheet(u"border:0px;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/maximize.svg", QSize(),
                      QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_maximize.setIcon(icon2)
        self.btn_maximize.setIconSize(QSize(14, 14))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.btn_exit.setText("")
        self.btn_collapse.setText("")
        self.btn_maximize.setText("")
    # retranslateUi
