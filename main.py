import sys
import os
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from ui_main_window import Ui_MainWindow
from page_switchers import switch_centerMenu


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.centerMenu = self.ui.centerMenu
        self.ui.leftMenu.setHidden(True)

# ------------------------
# Center menu
# ------------------------
        self.ui.centerMenu.setHidden(True)
        self.ui.pushButton_9.clicked.connect(
            lambda: self.switch_centerMenu_to_index(0))
        self.ui.pushButton_11.clicked.connect(
            lambda: self.switch_centerMenu_to_index(1))
        self.ui.pushButton_12.clicked.connect(
            lambda: self.switch_centerMenu_to_index(2))
        self.ui.pushButton_5.clicked.connect(
            lambda: self.switch_centerMenu_to_index(0))
        self.ui.pushButton_6.clicked.connect(
            lambda: self.switch_centerMenu_to_index(1))
        self.ui.pushButton_7.clicked.connect(
            lambda: self.switch_centerMenu_to_index(2))
# ------------------------
# mainContents
# ------------------------
    # ------------------------
    # mainPagesCont
    # ------------------------
        self.ui.pushButton_13.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.pushButton_14.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentIndex(1))
        self.ui.pushButton_15.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentIndex(2))
        self.ui.pushButton_16.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentIndex(3))
        self.ui.pushButton.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.pushButton_2.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentIndex(1))
        self.ui.pushButton_3.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentIndex(2))
        self.ui.pushButton_4.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentIndex(3))


# cache/tradnig_view_cache

        with open("templates/chart.html", "r", encoding="utf-8") as file:
            html_content = file.read()

        self.ui.web_view.setHtml(html_content)
    # ------------------------
    # rightMenu
    # ------------------------

    def switch_centerMenu_to_index(self, index):
        switch_centerMenu(self.ui, index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
