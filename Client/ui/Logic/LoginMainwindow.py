from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow
from PySide6 import QtCore
from Client.ui.Designer.ui_Login import Ui_LoginWindow
from Client.services.server_auth import AuthService
from Client.config import get_error_message, PURPOSE_REGISTER, PURPOSE_RETRIEVE
from .MainInterfaceMainwindow import MainInterfaceWindow

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.bind()
        self.ui.button_login_confirm.setEnabled(False)

    def bind(self):
        """信号与槽的连接"""
        # 切换界面
        self.ui.button_login.clicked.connect(self.move_to_login)
        self.ui.button_register.clicked.connect(self.move_to_register)
        self.ui.button_retrieve.clicked.connect(self.move_to_retrieve)

        # 登录
        self.ui.button_login_confirm.clicked.connect(self.validate_login)
        self.ui.line_login_username.textChanged.connect(self.validate_login_username)
        self.ui.line_login_password.textChanged.connect(self.validate_login_password)

        # 注册
        self.ui.button_register_confirm.clicked.connect(self.validate_register)
        self.ui.button_register_verificationGet.clicked.connect(self.get_register_verification)
        self.ui.line_register_username.textChanged.connect(self.validate_register_username)
        self.ui.line_register_password.textChanged.connect(self.validate_register_password)
        self.ui.line_register_okpassword.textChanged.connect(self.validate_register_okpassword)
        self.ui.line_register_email.textChanged.connect(self.validate_register_email)
        self.ui.line_register_verification.textChanged.connect(self.validate_register_verification)


        # 找回密码
        self.ui.button_retrievePassword_confirm.clicked.connect(self.validate_retrieve)
        self.ui.button_retrievePassword_verificationGet.clicked.connect(self.get_retrieve_verification)
        self.ui.line_retrievePassword_email.textChanged.connect(self.validate_retrieve_email)
        self.ui.line_retrievePassword_verification.textChanged.connect(self.validate_retrieve_verification)
        self.ui.line_retrievePassword_password.textChanged.connect(self.validate_retrieve_password)
        self.ui.line_retrievePassword_okpassword.textChanged.connect(self.validate_retrieve_okpassword)


# 切换界面
    def move_to_login(self):
        """切换到登陆界面"""
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(0)

    def move_to_register(self):
        """切换到注册界面"""
        self.ui.stackedWidget_2.setCurrentIndex(1)
        self.ui.stackedWidget.setCurrentIndex(1)

    def move_to_retrieve(self):
        """切换到找回密码界面"""
        self.ui.stackedWidget_2.setCurrentIndex(2)
        self.ui.stackedWidget.setCurrentIndex(2)

    def move_to_MainInterfaceWindow(self):
        """进入到主界面"""
        self.mainInterfaceWindow = MainInterfaceWindow()
        self.mainInterfaceWindow.show()
        self.close()

# 登录
    def validate_login_username(self):
        """检查登陆界面的用户名"""
        username = self.ui.line_login_username.text().strip()

        if not username:
            self.ui.line_login_username.setStyleSheet("border-bottom: 2px solid #5c9ef5;")
            self.ui.label_login_error.clear()
            self.update_login_button_state()
            return False

        valid, error_code = AuthService.validate_username(username)

        if not valid:
            self.ui.label_login_error.setText(get_error_message(error_code))
            self.ui.label_login_error.setStyleSheet("color: red;")
            self.ui.line_login_username.setStyleSheet("border-bottom: 2px solid red;")
            self.update_login_button_state()
            return False

        self.ui.label_login_error.clear()
        self.ui.line_login_username.setStyleSheet("border-bottom: 2px solid green;")
        self.update_login_button_state()
        return True

    def validate_login_password(self):
        """检查登陆界面的密码"""
        password = self.ui.line_login_password.text().strip()

        if not password:
            self.ui.line_login_password.setStyleSheet("border-bottom: 2px solid #5c9ef5;")
            self.ui.label_login_error.clear()
            self.update_login_button_state()
            return False

        valid, error_code = AuthService.validate_password(password)

        if not valid:
            self.ui.label_login_error.setText(get_error_message(error_code))  # 使用全局配置文件的错误信息
            self.ui.label_login_error.setStyleSheet("color: red;")
            self.ui.line_login_password.setStyleSheet("border-bottom: 2px solid red;")
            self.update_login_button_state()
            return False

        self.ui.label_login_error.clear()
        self.ui.line_login_password.setStyleSheet("border-bottom: 2px solid green;")
        self.update_login_button_state()
        return True

    def validate_login(self):
        """调用检查和登录请求方法"""
        username = self.ui.line_login_username.text().strip()
        password = self.ui.line_login_password.text().strip()

        if not username or not password:
            self.ui.label_login_error.setText("Username and password cannot be empty!")
            self.ui.label_login_error.setStyleSheet("color: red;")
            return

        response = AuthService.request_login(username, password)

        if response is None:
            self.ui.label_login_error.setText("Network error, please try again!")
            self.ui.label_login_error.setStyleSheet("color: red;")
            return

        try:
            data = response.json()
        except ValueError:
            self.ui.label_login_error.setText("Invalid server response.")
            self.ui.label_login_error.setStyleSheet("color: red;")
            return

        if response.status_code == 200:
            message = data.get("message", "Login successful!")
            color = "green"
            QTimer.singleShot(2000, self.move_to_MainInterfaceWindow)
        else:
            message = data.get("detail", "Invalid username or password!")
            color = "red"

        self.ui.label_login_error.setText(message)
        self.ui.label_login_error.setStyleSheet(f"color: {color};")

    def update_login_button_state(self):
        """更新登陆界面的按钮状态"""
        username_valid = AuthService.validate_username(self.ui.line_login_username.text().strip())
        password_valid = AuthService.validate_password(self.ui.line_login_password.text().strip())

        if username_valid and password_valid:
            self.ui.button_login_confirm.setEnabled(True)
        else:
            self.ui.button_login_confirm.setEnabled(False)

# 注册
    def validate_register_username(self):
        """检查注册界面的用户名"""
        username = self.ui.line_register_username.text().strip()
        if not username:
            self.ui.line_register_username.setStyleSheet("border-bottom: 2px solid #5c9ef5;")
            self.ui.label_register_error.clear()
            self.update_register_button_state()
            return False

        valid, error_code = AuthService.validate_username(username)

        if not valid:
            self.ui.label_register_error.setText(get_error_message(error_code))  # 使用全局配置文件的错误信息
            self.ui.label_register_error.setStyleSheet("color: red;")
            self.ui.line_register_username.setStyleSheet("border-bottom: 2px solid red;")
            self.update_register_button_state()
            return False

        self.ui.label_register_error.clear()
        self.ui.line_register_username.setStyleSheet("border-bottom: 2px solid green;")
        self.update_register_button_state()
        return True

    def validate_register_password(self):
        """检查注册界面的密码"""
        password = self.ui.line_register_password.text().strip()

        if not password:
            self.ui.line_register_password.setStyleSheet("border-bottom: 2px solid #5c9ef5;")
            self.ui.label_register_error.clear()
            self.update_register_button_state()
            return False

        valid, error_code = AuthService.validate_password(password)

        if not valid:
            self.ui.label_register_error.setText(get_error_message(error_code))  # 使用全局配置文件的错误信息
            self.ui.label_register_error.setStyleSheet("color: red;")
            self.ui.line_register_password.setStyleSheet("border-bottom: 2px solid red;")
            self.update_register_button_state()
            return False

        self.ui.label_register_error.clear()
        self.ui.line_register_password.setStyleSheet("border-bottom: 2px solid green;")
        self.update_register_button_state()

        return True

    def validate_register_okpassword(self):
        """检查注册界面的确认密码"""
        okpassword = self.ui.line_register_okpassword.text().strip()
        password = self.ui.line_register_password.text().strip()
        if not okpassword:
            self.ui.line_register_okpassword.setStyleSheet("border-bottom: 2px solid #5c9ef5;")
            self.ui.label_register_error.clear()
            self.update_register_button_state()
            return False

        valid, error_code = AuthService.validate_okpassword(password,okpassword)

        if not valid:
            self.ui.label_register_error.setText(get_error_message(error_code))
            self.ui.label_register_error.setStyleSheet("color: red;")
            self.ui.line_register_okpassword.setStyleSheet("border-bottom: 2px solid red;")
            self.update_register_button_state()
            return False

        self.ui.label_register_error.clear()
        self.ui.line_register_okpassword.setStyleSheet("border-bottom: 2px solid green;")
        self.update_register_button_state()

        return True

    def validate_register_email(self):
        """检查注册界面的邮箱"""
        email = self.ui.line_register_email.text().strip()
        if not email:
            self.ui.line_register_email.setStyleSheet("border-bottom: 2px solid #5c9ef5;")
            self.ui.label_register_error.clear()
            self.update_register_button_state()
            return False

        valid, error_code = AuthService.validate_email(email)

        if not valid:
            self.ui.label_register_error.setText(get_error_message(error_code))
            self.ui.label_register_error.setStyleSheet("color: red;")
            self.ui.line_register_email.setStyleSheet("border-bottom: 2px solid red;")
            self.update_register_button_state()
            return False

        self.ui.label_register_error.clear()
        self.ui.line_register_email.setStyleSheet("border-bottom: 2px solid green;")
        self.update_register_button_state()

        return True

    def validate_register_verification(self):
        """检查注册界面的验证码"""
        verification = self.ui.line_register_verification.text().strip()

        if not verification:
            self.ui.line_register_verification.setStyleSheet("border-bottom: 2px solid #5c9ef5;")
            self.ui.label_register_error.clear()
            self.update_register_button_state()
            return False

        valid, error_code = AuthService.validate_verification(verification)

        if not valid:
            self.ui.label_register_error.setText(get_error_message(error_code))
            self.ui.label_register_error.setStyleSheet("color: red;")
            self.ui.line_register_verification.setStyleSheet("border-bottom: 2px solid red;")
            self.update_register_button_state()
            return False

        self.ui.label_register_error.clear()
        self.ui.line_register_verification.setStyleSheet("border-bottom: 2px solid green;")
        self.update_register_button_state()
        return True

    def validate_register(self):
        """调用检查和注册请求方法"""
        username = self.ui.line_register_username.text().strip()
        password = self.ui.line_register_password.text().strip()
        okpassword = self.ui.line_register_okpassword.text().strip()
        email = self.ui.line_register_email.text().strip()
        verification = self.ui.line_register_verification.text().strip()

        if not username or not password or not okpassword or not email or not verification:
            self.ui.label_login_error.setText("Code cannot be empty!")
            self.ui.label_login_error.setStyleSheet("color: red;")
            return

        username_valid = self.validate_register_username()
        password_valid = self.validate_register_password()
        okpassword_valid = self.validate_register_okpassword()
        email_valid = self.validate_register_email()
        verification_valid = self.validate_register_verification()

        if username_valid and password_valid and okpassword_valid and email_valid and verification_valid:
            response = AuthService.request_register(username, password, okpassword, email, verification)

            if response is None:
                self.ui.label_register_error.setText("Network error, please try again!")
                self.ui.label_register_error.setStyleSheet("color: red;")
                return

            try:
                data = response.json()
            except ValueError:
                self.ui.label_register_error.setText("Invalid server response.")
                self.ui.label_register_error.setStyleSheet("color: red;")
                return

            if response.status_code == 200:
                message = data.get("message", "Register successful!")
                color = "green"
            else:
                message = data.get("detail", "Registration failed!")
                color = "red"

            self.ui.label_register_error.setText(message)
            self.ui.label_register_error.setStyleSheet(f"color: {color};")

    def get_register_verification(self):
        """获取注册界面的邮箱验证码"""
        email = self.ui.line_register_email.text().strip()

        if not email:
            self.ui.label_register_error.setText("Email cannot be empty!")
            self.ui.label_register_error.setStyleSheet("color: red;")
            return

        response = AuthService.request_verification(email,PURPOSE_REGISTER)

        if response is None:
            self.ui.label_register_error.setText("Network error, please try again!")
            self.ui.label_register_error.setStyleSheet("color: red;")
            return

        try:
            data = response.json()
        except ValueError:
            self.ui.label_register_error.setText("Failed to parse response data!")
            self.ui.label_register_error.setStyleSheet("color: red;")
            return

        if response.status_code == 200:
            message = data.get("message", "Verification email sent successfully!")
            color = "green"
        else:
            message = data.get("detail", "Failed to send verification code!")
            color = "red"

        self.ui.label_register_error.setText(message)
        self.ui.label_register_error.setStyleSheet(f"color: {color};")

    def update_register_button_state(self):
        """根据输入框的状态更新注册按钮的状态"""
        username_valid = AuthService.validate_username(self.ui.line_register_username.text().strip())
        password_valid = AuthService.validate_password(self.ui.line_register_password.text().strip())
        okpassword_valid = AuthService.validate_okpassword(self.ui.line_register_password.text().strip() ,self.ui.line_register_okpassword.text().strip())
        email_valid = AuthService.validate_email(self.ui.line_register_email.text().strip())
        verification_valid =  AuthService.validate_verification(self.ui.line_register_verification.text().strip())

        if username_valid and password_valid and okpassword_valid and email_valid and verification_valid:
            self.ui.button_login_confirm.setEnabled(True)
        else:
            self.ui.button_login_confirm.setEnabled(False)

# 找回密码
    def validate_retrieve_email(self):
        """检查找回密码界面的邮箱"""
        email = self.ui.line_retrievePassword_email.text().strip()
        if not email:
            self.ui.line_retrievePassword_email.setStyleSheet("border-bottom: 2px solid #5c9ef5;")
            self.ui.label_retrievePassword_error.clear()
            self.update_retrieve_button_state()
            return False

        valid, error_code = AuthService.validate_email(email)

        if not valid:
            self.ui.label_retrievePassword_error.setText(get_error_message(error_code))
            self.ui.label_retrievePassword_error.setStyleSheet("color: red;")
            self.ui.line_retrievePassword_email.setStyleSheet("border-bottom: 2px solid red;")
            self.update_retrieve_button_state()
            return False

        self.ui.label_retrievePassword_error.clear()
        self.ui.line_retrievePassword_email.setStyleSheet("border-bottom: 2px solid green;")
        self.update_retrieve_button_state()

        return True

    def validate_retrieve_verification(self):
        """检查找回密码界面的验证码"""
        verification = self.ui.line_retrievePassword_verification.text().strip()
        if not verification:
            self.ui.line_retrievePassword_verification.setStyleSheet("border-bottom: 2px solid #5c9ef5;")
            self.ui.label_retrievePassword_error.clear()
            self.update_retrieve_button_state()
            return False
        valid, error_code = AuthService.validate_verification(verification)
        if not valid:
            self.ui.label_retrievePassword_error.setText(get_error_message(error_code))
            self.ui.label_retrievePassword_error.setStyleSheet("color: red;")
            self.ui.line_retrievePassword_verification.setStyleSheet("border-bottom: 2px solid red;")
            self.update_retrieve_button_state()
            return False
        self.ui.label_retrievePassword_error.clear()
        self.ui.line_retrievePassword_verification.setStyleSheet("border-bottom: 2px solid green;")
        self.update_retrieve_button_state()
        return True

    def validate_retrieve_password(self):
        """检查找回密码界面的密码"""
        password = self.ui.line_retrievePassword_password.text().strip()
        if not password:
            self.ui.line_retrievePassword_password.setStyleSheet("border-bottom: 2px solid #5c9ef5;")
            self.ui.label_retrievePassword_error.clear()
            self.update_retrieve_button_state()
            return False
        valid, error_code = AuthService.validate_password(password)
        if not valid:
            self.ui.label_retrievePassword_error.setText(get_error_message(error_code))
            self.ui.label_retrievePassword_error.setStyleSheet("color: red;")
            self.ui.line_retrievePassword_password.setStyleSheet("border-bottom: 2px solid red;")
            self.update_retrieve_button_state()
            return False
        self.ui.label_retrievePassword_error.clear()
        self.ui.line_retrievePassword_password.setStyleSheet("border-bottom: 2px solid green;")
        self.update_retrieve_button_state()
        return True

    def validate_retrieve_okpassword(self):
        """检查找回密码界面的确认密码"""
        okpassword = self.ui.line_retrievePassword_okpassword.text().strip()
        password = self.ui.line_retrievePassword_password.text().strip()
        if not okpassword:
            self.ui.line_retrievePassword_okpassword.setStyleSheet("border-bottom: 2px solid #5c9ef5;")
            self.ui.label_retrievePassword_error.clear()
            self.update_retrieve_button_state()
            return False
        valid, error_code = AuthService.validate_okpassword(password, okpassword)
        if not valid:
            self.ui.label_retrievePassword_error.setText(get_error_message(error_code))
            self.ui.label_retrievePassword_error.setStyleSheet("color: red;")
            self.ui.line_retrievePassword_okpassword.setStyleSheet("border-bottom: 2px solid red;")
            self.update_retrieve_button_state()
            return False
        self.ui.label_retrievePassword_error.clear()
        self.ui.line_retrievePassword_okpassword.setStyleSheet("border-bottom: 2px solid green;")
        self.update_retrieve_button_state()
        return True

    def get_retrieve_verification(self):
        """获取找回密码界面的验证码"""
        email = self.ui.line_retrievePassword_email.text().strip()

        if not email:
            self.ui.label_retrievePassword_error.setText("Email cannot be empty!")
            self.ui.label_retrievePassword_error.setStyleSheet("color: red;")
            return

        print("email get successfully")
        response = AuthService.request_verification(email, PURPOSE_RETRIEVE)

        if response is None:
            self.ui.label_retrievePassword_error.setText("Network error, please try again!")
            self.ui.label_retrievePassword_error.setStyleSheet("color: red;")
            return

        try:
            data = response.json()
        except ValueError:
            self.ui.label_retrievePassword_error.setText("Failed to parse response data!")
            self.ui.label_retrievePassword_error.setStyleSheet("color: red;")
            return

        if response.status_code == 200:
            message = data.get("message", "Verification successful!")
            color = "green"
        else:
            message = data.get("detail", "Invalid verification code!")
            color = "red"

        self.ui.label_retrievePassword_error.setText(message)
        self.ui.label_retrievePassword_error.setStyleSheet(f"color: {color};")

    def validate_retrieve(self):
        """调用检查和找回密码请求方法"""
        email = self.ui.line_retrievePassword_email.text().strip()
        verification = self.ui.line_retrievePassword_verification.text().strip()
        password = self.ui.line_retrievePassword_password.text().strip()
        okpassword = self.ui.line_retrievePassword_okpassword.text().strip()

        if not email or not verification or not password or not okpassword:
            self.ui.label_retrievePassword_error.setText("code cannot be empty!")
            self.ui.label_retrievePassword_error.setStyleSheet("color: red;")
            return

        email_valid = self.validate_retrieve_email()
        verification_valid = self.validate_retrieve_verification()
        password_valid = self.validate_retrieve_password()
        okpassword_valid = self.validate_retrieve_okpassword()

        if email_valid and verification_valid and password_valid and okpassword_valid:
            response = AuthService.request_retrieve(email, verification, password, okpassword)

            if response is None:
                self.ui.label_retrievePassword_error.setText("Network error, please try again!")
                self.ui.label_retrievePassword_error.setStyleSheet("color: red;")
                return

            try:
                data = response.json()
            except ValueError:
                self.ui.label_retrievePassword_error.setText("Failed to parse response data!")
                self.ui.label_retrievePassword_error.setStyleSheet("color: red;")
                return

            if response.status_code == 200:
                message = data.get("message", "Password retrieve successfully!")
                color = "green"
            else:
                message = data.get("detail", "Failed to retrieve the password!")
                color = "red"

            self.ui.label_retrievePassword_error.setText(message)
            self.ui.label_retrievePassword_error.setStyleSheet(f"color: {color};")

    def update_retrieve_button_state(self):
        """更新找回密码界面的按钮状态"""
        email_valid = AuthService.validate_email(self.ui.line_retrievePassword_email.text().strip())
        verification_valid = AuthService.validate_verification(self.ui.line_retrievePassword_verification.text().strip())
        password_valid = AuthService.validate_password(self.ui.line_retrievePassword_password.text().strip())
        okpassword_valid = AuthService.validate_okpassword(self.ui.line_retrievePassword_password.text().strip(),
                                                     self.ui.line_retrievePassword_okpassword.text().strip())
        if email_valid and verification_valid and password_valid and okpassword_valid:
            self.ui.button_retrievePassword_confirm.setEnabled(True)
        else:
            self.ui.button_retrievePassword_confirm.setEnabled(False)





