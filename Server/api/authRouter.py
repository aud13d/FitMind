from fastapi import APIRouter
from ..schemas.auth import *
from ..services.authService import AuthService


router = APIRouter(prefix="/auth", tags=["Auth"])

# 登录
@router.post("/login")
async def login(user: LoginRequest):
    """接收客户端的登录请求"""
    response = await AuthService.login_user(username=user.username, password=user.password)
    return response

# 注册
@router.post("/register")
async def register(user: RegisterRequest):
    """接收客户端的注册请求"""
    response = await AuthService.register_user(
        email=user.email,
        username=user.username,
        password=user.password,
        confirm_password=user.okpassword,
        verification=user.verification
    )

    return response

#找回密码
@router.post("/retrieve_password")
async def retrieve(user: RetrieveRequest):
    """接收客户端的找回密码请求"""
    response = await AuthService.retrieve_password(
        email=user.email,
        verification=user.verification,
        password=user.password,
        confirm_password=user.okpassword
    )
    return response

# 发送验证码
@router.post("/send_verification")
async def send_verification(user: SendVerificationRequest):
    """接收客户端的发送验证码请求"""
    response = await AuthService.send_verification_code(user.email,user.purpose)
    return response



