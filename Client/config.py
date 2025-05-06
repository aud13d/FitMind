# 错误码
ERROR_CODES = {
    "ERROR_USERNAME_TOO_SHORT": 1001, #用户名太短
    "ERROR_USERNAME_NOT_ALNUM": 1002, #用户名不是字母和数字
    "ERROR_USERNAME_CONTAINS_SPACE": 1003, #用户名包含空格

    "ERROR_PASSWORD_TOO_SHORT": 2001, #密码太短
    "ERROR_PASSWORD_NO_LETTER": 2002, #密码没有字母
    "ERROR_PASSWORD_NO_DIGIT": 2003, #密码没有数字
    "ERROR_PASSWORD_NO_SPECIAL_CHAR": 2004, #密码没有特殊字符
    "ERROR_PASSWORD_CONTAINS_SPACE": 2005, #密码包含空格
    "ERROR_PASSWORD_NOT_MATCH_OKPASSWORD":2006, #密码和确认密码不匹配

    "ERROR_EMAIL_INVALID_FORMAT": 3001, #邮箱格式无效

    "ERROR_VERIFICATION_INVALID_FORMAT": 4001, #验证码格式无效
}

# 错误信息
ERROR_MESSAGES = {
    #用户名相关
    1001: "Username must be at least 4 characters!",
    1002: "Username must be alphanumeric!",
    1003: "Username cannot contain spaces!",

    #密码相关
    2001: "Password must be at least 6 characters!",
    2002: "Password must contain at least one letter!",
    2003: "Password must contain at least one digit!",
    2004: "Password must contain at least one special character!",
    2005: "Password cannot contain spaces!",
    2006: "Password and confirm password do not match!",

    #邮箱相关
    3001: "Invalid email format!",

    #验证码相关
    4001: "Invalid verification code format!",

    #通用错误
    400: "Invalid request data!",
    401: "Unauthorized! Please check your credentials.",
    403: "Forbidden! You don't have permission.",
    404: "services not found! Please check the API URL.",
    500: "Internal services Error! Please try again later.",
}

# 获取错误信息
def get_error_message(error_code):
    return ERROR_MESSAGES.get(error_code, "An unexpected error occurred!")

# 网络请求
BASE_URL = "http://127.0.0.1:8000/auth"
API_TIMEOUT = 10
PURPOSE_REGISTER = "register"
PURPOSE_RETRIEVE = "retrieve"

# 图标路径
CancelTrainingQDialog_IconPath = ":/icons/icon/疑惑.png"
FinishTrainingQDialog_IconPath = ":/icons/icon/a-haoping1.png"
MoveAddActionQDialog_IconPath = ":/icons/icon/移动.png"
GoAddActionQDialog_IconPath =":/icons/icon/back.png"