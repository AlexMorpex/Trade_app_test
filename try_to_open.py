import sys
import os
from PySide6.QtWidgets import QApplication, QWidget
from main import MainWindow
from ui_Logger_window import Ui_centralWidget
# Запуск файла main.py
# subprocess.Popen(["python", "main.py"])
# try:
#     os.system('python "main.py"')
# except Exception as e:
#     print(e)


class Logger(QWidget):
    def __init__(self):
        super(Logger, self).__init__()
        self.ui = Ui_centralWidget()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = Ui_centralWidget()
    window.show()
    sys.exit(app.exec())
