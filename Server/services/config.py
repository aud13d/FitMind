# 邮箱配置
SMTP_HOST = "smtp.qq.com"
SMTP_PORT = 465
SMTP_USER = "3048484140@qq.com"
SMTP_PASSWORD = "dtzqtkefrjhgddbh"
SMTP_EMAIL_SUBTYPE = "html"

# 验证码邮件主题
EMAIL_VERIFICATION_SUBJECT = "FitMind 🔐 Verification Code"

# 验证码邮件正文模板
EMAIL_VERIFICATION_BODY = """
<p style="font-size: 16px; color: #333;">😊Dear User, 🌟</p>
<p style="font-size: 16px; color: #555;">Thank you for using <strong>FitMind</strong>! 
To ensure the safety of your account, we need to verify your identity. 🛡️</p>
<p style="font-size: 16px; color: #007BFF;"><strong>Your verification code is: {code} 🔑</strong></p>
<p style="font-size: 16px; color: #555;">Please enter the code within <span style="color: red;">5 minutes ⏳</span> 
to complete your process. The code is valid for only one use!</p>
<p style="font-size: 16px; color: #555;">If you did not request this action, please disregard this email. ❌</p>
<p style="font-size: 16px; color: #555;">Wishing you a great experience with <strong>FitMind</strong>! 🎉</p>
"""

# 目的请求
PURPOSE_REGISTER = "register"
PURPOSE_RETRIEVE = "retrieve"

# 验证码有效期（秒）
CODE_EXPIRATION = 300

# 错误提示

# 用户名相关
USERNAME_ALREADY_EXISTS = "Username already exists!"
USERNAME_MIN_LENGTH_AND_ALPHANUMERIC = "Username must be at least 4 characters,\n and only contain letters and numbers!"
USER_NOT_FOUND = "User not found!"

# 邮箱相关
EMAIL_ALREADY_EXISTS = "Email already exists!"
EMAIL_DOES_NOT_EXIST = "Email does not exist!"
EMAIL_ALREADY_EXISTS_AGAIN = "Email already exists!"
EMAIL_DOES_NOT_EXIST_AGAIN = "Email does not exist!"
INVALID_EMAIL_FORMAT = "Invalid email format!"

# 密码相关
PASSWORD_MIN_LENGTH = "Password must be at least 6 characters long!"
PASSWORD_CONTAINS_LETTER = "Password must contain at least one letter!"
PASSWORD_CONTAINS_NUMBER = "Password must contain at least one number!"
PASSWORD_CONTAINS_SPECIAL_CHAR = "Password must contain at least one special character\n (@, #, $, %, etc.)!"
PASSWORD_NO_SPACES = "Password cannot contain spaces!"
PASSWORDS_DO_NOT_MATCH = "Passwords do not match"

# 验证码相关
VERIFICATION_CODE_MIN_LENGTH = "Verification code must be 4 digits!"
VERIFICATION_CODE_EXPIRED_OR_NOT_EXIST = "Verification code has expired or does not exist!"
VERIFICATION_CODE_INCORRECT = "Verification code is incorrect!"

# 验证相关
INVALID_USERNAME_OR_PASSWORD = "Invalid username or password!"

# 训练相关
TRAINING_ACTION_EXIST = "Training action cannot be empty!"
TRAINING_START_DATE_AFTER_END_DATE = "The start time cannot be later than the end time!"
TRAINING_DURATION_MUST_BE_POSITIVE = "Training duration must be positive!"
TRAINING_CREATE_FAILED = "Training creation failed!"

# 有氧相关
AEROBIC_START_DATE_AFTER_END_DATE = "The start time cannot be later than the end time!"
AEROBIC_DURATION_MUST_BE_POSITIVE = "Aerobics duration must be positive!"
AEROBIC_INTERVAL_REMINDER_INVALID = "Interval reminder must be a positive integer!"
AEROBIC_INTERVAL_ITEMS_REQUIRED = "Interval items are required!"
AEROBIC_CREATE_FAILED = "Aerobic creation failed!"

# 休息相关
REST_CREATE_FAILED = "Rest creation failed!"

# 运动数据相关
TRAINING_SPORTS_INFO_NOT_EXIST = "Sports info does not exist!"
AEROBIC_SPORTS_INFO_NOT_EXIST = "Sports info does not exist!"
REST_SPORTS_INFO_NOT_EXIST = "Sports info does not exist!"

# 成功提示
VERIFICATION_SENT = "Verification has been sent to your email!"
VERIFICATION_CODE_FAILED = "Verification code could not be sent!"
REGISTRATION_SUCCESSFULLY = "Registration successfully!"
PASSWORD_RESET_SUCCESSFULLY = "Password reset successfully!"
LOGIN_SUCCESSFULLY = "Login successfully!"
TRAINING_FINISH = "Training finished successfully!"
AEROBIC_CONFIRM = "Aerobic confirmed successfully!"
REST_SAVE="Rest saved successfully!"


