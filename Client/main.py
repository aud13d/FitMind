from PySide6 import QtCore
from PySide6.QtWidgets import QApplication
import sys
from Client.ui.LoginMainwindow import LoginWindow
from Client.ui.MainInterfaceMainwindow import MainInterfaceWindow
from Client.ui.NewTrainWidget import NewTrainWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewTrainWidget()
    window.show()
    sys.exit(app.exec())