class UserSession:
    user_id = None
    username = None

    @classmethod
    def set_user(cls, user_id, username=None, token=None):
        cls.user_id = user_id
        cls.username = username
        cls.token = token # 后面改用JWT令牌

    @classmethod
    def clear(cls):
        cls.user_id = None
        cls.username = None
        cls.token = None

    @classmethod
    def get_user_id(cls):
        return cls.user_id

    @classmethod
    def get_username(cls):
        return cls.username

    @classmethod
    def get_token(cls):
        return cls.token
