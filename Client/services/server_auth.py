import re
import requests
from ..config import ERROR_CODES,BASE_URL,API_TIMEOUT

class AuthService:
    @staticmethod
    def validate_username(username):
        """验证用户名格式"""
        if len(username) < 4:
            return False, ERROR_CODES["ERROR_USERNAME_TOO_SHORT"]
        if not username.isalnum():
            return False, ERROR_CODES["ERROR_USERNAME_NOT_ALNUM"]
        if ' ' in username:
            return False, ERROR_CODES["ERROR_USERNAME_CONTAINS_SPACE"]
        return True, None

    @staticmethod
    def validate_password(password):
        """验证密码格式"""
        if len(password) < 6:
            return False, ERROR_CODES["ERROR_PASSWORD_TOO_SHORT"]
        if not re.search(r'[A-Za-z]', password):
            return False, ERROR_CODES["ERROR_PASSWORD_NO_LETTER"]
        if not re.search(r'[0-9]', password):
            return False, ERROR_CODES["ERROR_PASSWORD_NO_DIGIT"]
        if not re.search(r'[@#$%^&+=!]', password):
            return False, ERROR_CODES["ERROR_PASSWORD_NO_SPECIAL_CHAR"]
        if ' ' in password:
            return False, ERROR_CODES["ERROR_PASSWORD_CONTAINS_SPACE"]
        return True, None

    @staticmethod
    def validate_okpassword(password, confirm_password):
        """验证确认密码是否与密码一致"""
        if password != confirm_password:
            return False, ERROR_CODES["ERROR_PASSWORD_NOT_MATCH_OKPASSWORD"]
        return True, None

    @staticmethod
    def validate_verification(verification):
        """验证验证码格式"""
        if not re.match(r'^\d{4}$', verification):
            return False, ERROR_CODES["ERROR_VERIFICATION_INVALID_FORMAT"]
        return True,None

    @staticmethod
    def validate_email(email):
        """验证邮箱格式"""
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            return False, ERROR_CODES["ERROR_EMAIL_INVALID_FORMAT"]

        return True,None

    @staticmethod
    def request_login(username, password):
        """向服务器发送登录请求"""
        url = f"{BASE_URL}/auth/login"
        data = {"username": username, "password": password}
        try:
            response = requests.post(url, json=data, timeout=API_TIMEOUT)
            print("服务器返回的内容:", response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"登录请求错误: {e}")
            return None

    @staticmethod
    def request_register(username, password, okpassword, email, verification):
        """向服务器发送注册请求"""
        url = f"{BASE_URL}/auth/register"
        data = {
            "email": email,
            "username": username,
            "password": password,
            "okpassword": okpassword,
            "verification": verification
        }

        try:
            response = requests.post(url, json=data,timeout=API_TIMEOUT)
            print("服务器返回的内容:", response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"注册请求出错: {e}")
            return None

    @staticmethod
    def request_retrieve(email, verification, password, okpassword):
        """向服务器发送找回密码请求"""
        url = f"{BASE_URL}/auth/retrieve_password"
        data = {
            "email": email,
            "verification": verification,
            "password": password,
            "okpassword": okpassword
        }

        try:
            response = requests.post(url, json=data,timeout=API_TIMEOUT)
            print("服务器返回的内容:", response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"找回密码请求错误: {e}")
            return None

    @staticmethod
    def request_verification(email,purpose):
        """向服务器发送验证码请求"""
        url = f"{BASE_URL}/auth/send_verification"
        data = {
            "email": email,
            "purpose": purpose
        }

        try:
            response = requests.post(url, json=data,timeout=API_TIMEOUT)
            print("服务器返回的内容:", response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"验证请求错误: {e}")
            return None

