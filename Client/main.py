from PySide6.QtWidgets import QApplication
import sys
from Client.ui.Logic.MainInterfaceMainwindow import MainInterfaceWindow
from Client.ui.Logic.AddActionDialog import AddActionDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainInterfaceWindow()
    window.show()
    sys.exit(app.exec())