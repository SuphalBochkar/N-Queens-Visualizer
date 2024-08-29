# main.py

import sys
from PyQt5.QtWidgets import QApplication
from input import InputWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    input_window = InputWindow()
    input_window.show()
    sys.exit(app.exec_())
