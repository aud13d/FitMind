from tortoise.models import Model
from tortoise import fields
import bcrypt

class User(Model):
    id = fields.IntField(pk=True)  # id 会自动分配
    email = fields.CharField(max_length=255, unique=True)
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "users"

    @classmethod
    async def create_user(cls, email, username, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = await cls.create(
            email=email,
            username=username,
            password=hashed_password.decode('utf-8')  # 存储为字符串
        )
        return user

    @classmethod
    async def verify_password(cls, username, password):
        user = await cls.filter(username=username).first()
        if user is None:
            return False  # 用户不存在

        return bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))

    @classmethod
    async def update_password(cls, email, new_password):
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        result = await cls.filter(email=email).update(password=hashed_password.decode('utf-8'))

