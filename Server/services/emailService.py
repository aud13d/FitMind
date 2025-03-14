import aiosmtplib
from email.message import EmailMessage
from .config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, EMAIL_VERIFICATION_SUBJECT, EMAIL_VERIFICATION_BODY , SMTP_EMAIL_SUBTYPE , VERIFICATION_CODE_FAILED
import random
import string
from fastapi import HTTPException
from ..database.redisClient import RedisClient

class EmailService:
    def generate_verification_code(length: int = 4, digits_only: bool = True) -> str:
        characters = string.digits if digits_only else string.ascii_uppercase + string.digits
        return ''.join(random.choices(characters, k=length))

    @staticmethod
    async def get_verification_code(email: str):
        code = EmailService.generate_verification_code(digits_only=True)

        await RedisClient.set(email, code, expire=300)

        email_subject = EMAIL_VERIFICATION_SUBJECT
        email_body = EMAIL_VERIFICATION_BODY.format(code=code)

        email_sent = await EmailService.send_email(email, email_subject, email_body)

        if email_sent:
            return
        else:
            raise HTTPException(status_code=500, detail=VERIFICATION_CODE_FAILED)

    @staticmethod
    async def send_email(recipient_email: str, subject: str, body: str):
        # 创建邮件对象
        message = EmailMessage()
        message.set_content(body, subtype=SMTP_EMAIL_SUBTYPE)  # 邮件内容是 HTML 格式
        message["Subject"] = subject
        message["From"] = SMTP_USER
        message["To"] = recipient_email

        try:
            # 使用 aiosmtplib 发送邮件
            async with aiosmtplib.SMTP(
                    hostname=SMTP_HOST, port=SMTP_PORT, use_tls=True  # 465 端口需要 use_tls=True
            ) as smtp:
                await smtp.login(SMTP_USER, SMTP_PASSWORD)
                await smtp.send_message(message)
            return True


        except Exception as e:
            print(f"邮件发送失败: {e}")
            print(f"完整的错误: {e.__class__}, {str(e)}")
            raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")


