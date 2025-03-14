from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from Server.api.authRouter import router as auth_router
from Server.database.postgreSql import Database
from Server.database.redisClient import RedisClient

#Lifespan(生命周期事件)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时的操作
    print("Starting up")
    await Database.init()
    await RedisClient.get_client()
    yield  # FastAPI 会自动处理 shutdown 事件
    # 关闭时的操作
    await Database.close()
    await RedisClient.close()
    print("Shutting down")

app = FastAPI(lifespan=lifespan)

# 注册路由
app.include_router(auth_router)

if __name__ == "__main__":
    uvicorn.run("main.py:app", host="127.0.0.1", port=8000, reload=True)

#uvicorn Server.main:app --reload
#redis-server.exe redis.conf

