from tortoise.models import Model
from tortoise import fields
import bcrypt
from datetime import datetime

class User(Model):
    id = fields.IntField(pk=True)  # id 会自动分配
    email = fields.CharField(max_length=255, unique=True)
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    logged_in = fields.BooleanField(default=False)  # 新增的字段，表示用户是否已登录
    login_at = fields.DatetimeField(null=True)  # 用于记录上次登录的时间，允许为 null

    class Meta:
        table = "users"

    @classmethod
    async def create_user(cls, email, username, password):
        """创建新用户"""
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = await cls.create(
            email=email,
            username=username,
            password=hashed_password.decode('utf-8'),  # 存储为字符串
            logged_in = False  # 保持登录状态为 False
        )
        return user

    @classmethod
    async def verify_password(cls, username, password):
        """验证用户密码"""
        user = await cls.filter(username=username).first()
        if user is None:
            return False  # 用户不存在

        return bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))

    @classmethod
    async def update_password(cls, email, new_password):
        """更新用户密码"""
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        return await cls.filter(email=email).update(password=hashed_password.decode('utf-8'))

    @classmethod
    async def set_logged_in(cls, username):
        """将用户的登录状态设置为 True"""
        user = await cls.filter(username=username).first()
        if not user:
            return False
        user.logged_in = True  # 将用户的登录状态设置为 True
        user.login_at = datetime.now()
        await user.save()  # 保存更改
        return True  # 如果没有找到用户，返回 False


    @classmethod
    async def set_logged_out(cls, username):
        """将用户的登录状态设置为 False"""
        user = await cls.filter(username=username).first()
        if not user:
            return True

        user.logged_in = False  # 将用户的登录状态设置为 False

        await user.save()  # 保存更改
        return True  # 如果没有找到用户，返回 False
