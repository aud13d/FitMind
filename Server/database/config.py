# 模型
TORTOISE_MODELS = ["Server.models.user",
                   "Server.models.userSportsInfo",
                   "Server.models.train",
                   "Server.models.trainItem",
                   "Server.models.aerobic",
                   "Server.models.aerobicItem",
                   "Server.models.rest",
                   "Server.models.userBodyInfo",
                   "Server.models.weight",
                   "Server.models.weightHistory",
                   "Server.models.circumference",]  # 将模型路径添加到列表中

# PostgreSQL数据库
DATABASE_CONFIG = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.asyncpg',  # 使用 asyncpg 作为 PostgreSQL 驱动
            'credentials': {
                'host': '127.0.0.1',
                'port': 5432,
                'user': 'postgres',
                'password': '123456',
                'database': 'FitMind'
            }
        }
    },
    'apps': {
        "models": {
            "models": TORTOISE_MODELS,
            "default_connection": "default",
        }
    }
}

# Redis数据库
REDIS_HOST: str = "127.0.0.1"
REDIS_PORT: int = 6379
REDIS_DB: int = 0
