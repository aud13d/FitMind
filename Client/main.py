from PySide6.QtWidgets import QApplication
import sys
from Client.ui.LoginMainwindow import LoginWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())