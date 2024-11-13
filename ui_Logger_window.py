# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'Logger.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_file_rc


class Ui_centralWidget(object):
    def setupUi(self, centralWidget):
        if not centralWidget.objectName():
            centralWidget.setObjectName(u"centralWidget")
        centralWidget.resize(561, 398)
        centralWidget.setStyleSheet(u"background-color:#04202C;\n"
                                    "")
        self.horizontalLayout = QHBoxLayout(centralWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Login = QWidget(centralWidget)
        self.Login.setObjectName(u"Login")
        self.verticalLayout = QVBoxLayout(self.Login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.Login)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:white;")

        self.horizontalLayout_2.addWidget(self.label)

        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.Login)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.login_field = QLineEdit(self.widget_2)
        self.login_field.setObjectName(u"login_field")
        self.login_field.setMinimumSize(QSize(150, 40))
        self.login_field.setMaximumSize(QSize(150, 16777215))
        self.login_field.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.login_field.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.login_field.setStyleSheet(u"border:1px solid white;\n"
                                       "border-radius:10px;\n"
                                       "padding-left:5px;\n"
                                       "padding-right:5px;\n"
                                       "padding-top:5px;\n"
                                       "padding-bottom:5px;\n"
                                       "color:White;")
        self.login_field.setFrame(True)

        self.verticalLayout_2.addWidget(self.login_field)

        self.password_field = QLineEdit(self.widget_2)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setMinimumSize(QSize(150, 40))
        self.password_field.setMaximumSize(QSize(150, 16777215))
        self.password_field.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.password_field.setStyleSheet(u"border:1px solid white;\n"
                                          "border-radius:10px;\n"
                                          "padding-left:5px;\n"
                                          "padding-right:5px;\n"
                                          "padding-top:5px;\n"
                                          "padding-bottom:5px;\n"
                                          "color:White;")
        self.password_field.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.password_field)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color:white;")

        self.verticalLayout_2.addWidget(self.label_4)

        self.verticalLayout.addWidget(
            self.widget_2, 0, Qt.AlignmentFlag.AlignVCenter)

        self.widget_3 = QWidget(self.Login)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton = QPushButton(self.widget_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border:1px solid white;\n"
                                      "border-radius:10px;\n"
                                      "padding-left:5px;\n"
                                      "padding-right:5px;\n"
                                      "padding-top:5px;\n"
                                      "padding-bottom:5px;\n"
                                      "color:White;")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)

        self.verticalLayout_5.addWidget(self.pushButton)

        self.verticalLayout_4.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color:white;")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color:white;")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.verticalLayout_4.addWidget(self.widget_5)

        self.verticalLayout.addWidget(self.widget_3)

        self.horizontalLayout.addWidget(self.Login)

        self.Logo = QWidget(centralWidget)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setMinimumSize(QSize(290, 380))
        self.Logo.setMaximumSize(QSize(290, 380))
        self.verticalLayout_3 = QVBoxLayout(self.Logo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.logo_field = QLabel(self.Logo)
        self.logo_field.setObjectName(u"logo_field")
        self.logo_field.setPixmap(QPixmap(u":/Logo/icons/right_logo2.png"))
        self.logo_field.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.logo_field)

        self.horizontalLayout.addWidget(self.Logo)

        self.retranslateUi(centralWidget)

        self.pushButton.setDefault(False)

        QMetaObject.connectSlotsByName(centralWidget)
    # setupUi

    def retranslateUi(self, centralWidget):
        centralWidget.setWindowTitle(
            QCoreApplication.translate("centralWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate(
            "centralWidget", u"Login", None))
        self.login_field.setText("")
        self.login_field.setPlaceholderText(
            QCoreApplication.translate("centralWidget", u"Login", None))
        self.password_field.setText("")
        self.password_field.setPlaceholderText(
            QCoreApplication.translate("centralWidget", u"Password", None))
        self.label_4.setText(QCoreApplication.translate(
            "centralWidget", u"I forgot password or can't sign in", None))
        self.pushButton.setText(QCoreApplication.translate(
            "centralWidget", u"Sign in", None))
        self.label_3.setText(QCoreApplication.translate(
            "centralWidget", u"Do not have an account?", None))
        self.label_2.setText(QCoreApplication.translate(
            "centralWidget", u"Sign up", None))
        self.logo_field.setText("")
    # retranslateUi
