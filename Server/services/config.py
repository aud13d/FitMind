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

# 体重相关
CURRENT_WEIGHT_CREATE_FAILED = "Current weight creation failed!"
TARGET_WEIGHT_CREATE_FAILED = "Target weight creation failed!"
BODY_FAT_RATE_CREATE_FAILED = "Body fat rate creation failed!"
CURRENT_WEIGHT_NOT_EXIST = "Current weight does not exist!"
TARGET_WEIGHT_NOT_EXIST = "Target weight does not exist!"
CURRENT_FAT_NOT_EXIST = "Current fat does not exist!"
WEIGHT_HISTORY_NOT_EXIST = "Weight history does not exist!"
BODY_FAT_RATE_HISTORY_NOT_EXIST = "Body fat rate history does not exist!"

# 围度相关
SAVE_CURRENT_CIRCUMFERENCE_FAILED = "Save current circumference failed!"
INVALID_PART = "Invalid part!"
CIRCUMFERENCE_HISTORY_NOT_EXIST = "Circumference history does not exist!"
CIRCUMFERENCE_RECORD_NOT_EXIST = "Circumference record does not exist!"

# 身体数据相关
BODY_INFO_NOT_EXIST = "Body info does not exist!"

# 饮食相关
MEAL_FOOD_LIST_EMPTY = "Meal food list cannot be empty!"
MEAL_USER_DIET_INFO_NOT_FOUND = "Meal user diet info not found!"

# 饮食数据相关



# 成功提示
VERIFICATION_SENT = "Verification has been sent to your email!"
VERIFICATION_CODE_FAILED = "Verification code could not be sent!"
REGISTRATION_SUCCESSFULLY = "Registration successfully!"
PASSWORD_RESET_SUCCESSFULLY = "Password reset successfully!"
LOGIN_SUCCESSFULLY = "Login successfully!"
TRAINING_FINISH = "Training finished successfully!"
AEROBIC_CONFIRM = "Aerobic confirmed successfully!"
REST_SAVE="Rest saved successfully!"
TARGET_WEIGHT_CREATE_SUCCESSFULLY = "Target weight created successfully!"
CURRENT_WEIGHT_CREATE_SUCCESSFULLY = "Current weight created successfully!"
BODY_FAT_RATE_CREATE_SUCCESSFULLY = "Body fat rate created successfully!"
CURRENT_WEIGHT_GET_SUCCESSFULLY = "Current weight get successfully!"
TARGET_WEIGHT_GET_SUCCESSFULLY = "Target weight get successfully!"
CURRENT_BODY_FAT_RATE_GET_SUCCESSFULLY = "Current fat get successfully!"
WEIGHT_HISTORY_GET_SUCCESSFULLY = "Weight history get successfully!"
BODY_FAT_RATE_HISTORY_GET_SUCCESSFULLY = "Body fat rate history get successfully!"
WEIGHT_HISTORY_DELETED_SUCCESSFULLY = "Weight history deleted successfully!"
BODY_FAT_RATE_HISTORY_DELETED_SUCCESSFULLY = "Body fat rate history deleted successfully!"
CURRENT_CIRCUMFERENCE_SAVE_SUCCESSFULLY = "Current circumference saved successfully!"
CIRCUMFERENCE_HISTORY_GET_SUCCESSFULLY = "Circumference history get successfully!"
CIRCUMFERENCE_RECORD_DELETE_SUCCESSFULLY = "Circumference record deleted successfully!"
MEAL_ADD_SUCCESS = "Meal add success!"
