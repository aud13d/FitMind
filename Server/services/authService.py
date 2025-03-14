import re
from fastapi import HTTPException
from ..services.emailService import EmailService
from ..services.dataService import DataService
from .config import *


class AuthService:
    @staticmethod
    async def register_user(email: str, username: str, password: str, confirm_password: str, verification: str):
        await AuthService.validate_email(email)
        await AuthService.validate_username(username)
        await AuthService.validate_password(password, confirm_password)
        await AuthService.validate_verification_code(email, verification)

        existing_email = await DataService.check_email_exists(email)
        if existing_email:
            raise HTTPException(status_code=400, detail=EMAIL_ALREADY_EXISTS)

        existing_username = await DataService.check_username_exists(username)
        if existing_username:
            raise HTTPException(status_code=400, detail=USERNAME_ALREADY_EXISTS)

        await DataService.create_new_user(email, username, password)
        print("User registered successfully")
        return {"message": REGISTRATION_SUCCESSFULLY, "email": email, "username": username}

    @staticmethod
    async def login_user(username: str, password: str):
        await AuthService.validate_username(username)
        await AuthService.validate_password(password)

        if not await DataService.verify_user_password(username, password):
            raise HTTPException(status_code=400, detail=INVALID_USERNAME_OR_PASSWORD)

        print("User logged in successfully")
        return {"message": LOGIN_SUCCESSFULLY}

    @staticmethod
    async def retrieve_password(email: str, verification: str, password: str, confirm_password: str):
        await AuthService.validate_email(email)
        await AuthService.validate_verification_code(email,verification)
        await AuthService.validate_password(password, confirm_password)

        existing_email = await DataService.check_email_exists(email)
        if not existing_email:
            raise HTTPException(status_code=400, detail=EMAIL_DOES_NOT_EXIST)

        await DataService.update_user_password(email, password)
        print("Password reset successfully")
        return {"message": PASSWORD_RESET_SUCCESSFULLY, "email": email}


    @staticmethod
    async def validate_email(email: str):
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise HTTPException(status_code=400, detail=INVALID_EMAIL_FORMAT)

    @staticmethod
    async def validate_username(username: str):
        if len(username) < 4 or not username.isalnum() or ' ' in username:
            raise HTTPException(status_code=400, detail=USERNAME_MIN_LENGTH_AND_ALPHANUMERIC)

    @staticmethod
    async def validate_password(password: str, confirm_password: str = None):
        if len(password) < 6:
            raise HTTPException(status_code=400, detail=PASSWORD_MIN_LENGTH )

        if not re.search(r'[A-Za-z]', password):
            raise HTTPException(status_code=400, detail=PASSWORD_CONTAINS_LETTER)

        if not re.search(r'[0-9]', password):
            raise HTTPException(status_code=400, detail=PASSWORD_CONTAINS_NUMBER)

        if not re.search(r'[@#$%^&+=!]', password):
            raise HTTPException(status_code=400, detail=PASSWORD_CONTAINS_SPECIAL_CHAR)

        if ' ' in password:
            raise HTTPException(status_code=400, detail=PASSWORD_NO_SPACES)

        if confirm_password is not None and password != confirm_password:
            raise HTTPException(status_code=400, detail=PASSWORDS_DO_NOT_MATCH)

    @staticmethod
    async def validate_verification_code(email: str, code: str):
        if not re.match(r'^\d{4}$', code):
            raise HTTPException(status_code=400, detail=VERIFICATION_CODE_MIN_LENGTH)

        # 从 Redis 获取存储的验证码
        stored_code = await DataService.get_verification_code_from_redis(email)

        print(f"Stored code: {stored_code}")

        if not stored_code:
            raise HTTPException(status_code=400, detail=VERIFICATION_CODE_EXPIRED_OR_NOT_EXIST)

        if stored_code != code:
            raise HTTPException(status_code=400, detail=VERIFICATION_CODE_INCORRECT)

        # 验证成功后，删除存储的验证码
        await  DataService.delete_verification_code_from_redis(email)

        return True

    @staticmethod
    async def send_verification_code(email: str,purpose: str):
        if purpose == PURPOSE_REGISTER:
            existing_email = await DataService.check_email_exists(email)

            if existing_email:
                raise HTTPException(status_code=400, detail=EMAIL_ALREADY_EXISTS_AGAIN)

        if purpose == PURPOSE_RETRIEVE:
            existing_email = await DataService.check_email_exists(email)
            if not existing_email:
                raise HTTPException(status_code=400, detail=EMAIL_DOES_NOT_EXIST_AGAIN)

        await EmailService.get_verification_code(email)

        return {"message": VERIFICATION_SENT}







