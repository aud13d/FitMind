from pydantic import BaseModel, EmailStr

class RegisterRequest(BaseModel):
    """注册请求体"""
    email: EmailStr
    username: str
    password: str
    okpassword: str
    verification: str

class LoginRequest(BaseModel):
    """登录请求体"""
    username: str
    password: str

class RetrieveRequest(BaseModel):
    """找回密码请求体"""
    email: EmailStr
    verification: str
    password: str
    okpassword: str

class SendVerificationRequest(BaseModel):
    """发送验证码请求体"""
    email: EmailStr
    purpose: str