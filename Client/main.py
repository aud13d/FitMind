from PySide6.QtWidgets import QApplication
import sys
from Client.ui.Logic.MainInterfaceMainwindow import MainInterfaceWindow
from Client.ui.Logic.LoginMainwindow import LoginWindow
from Client.ui.Logic.ImplementAerobicDialog import ImplementAerobicDialog


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())