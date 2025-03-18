from PySide6.QtWidgets import QApplication
import sys
from Client.ui.LoginMainwindow import LoginWindow
from Client.ui.MainInterfaceMainwindow import MainInterfaceWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainInterfaceWindow()
    window.show()
    sys.exit(app.exec())