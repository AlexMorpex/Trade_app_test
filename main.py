import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPalette, QColor
from ui_main_window import Ui_MainWindow
from PySide6.QtCore import Qt, QPoint


class AppName(QMainWindow):

    def __init__(self):
        super(AppName, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = AppName()
    window.show()
    sys.exit(app.exec())
