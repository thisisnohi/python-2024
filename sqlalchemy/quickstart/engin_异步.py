import asyncio

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

# 创建数据库引擎
# echo=True 参数表示连接发出的 SQL 将被记录到标准输出。
# asyncmy 为异步连接驱动
engine = create_async_engine('mysql+asyncmy://root:root1234@127.0.0.1:3306/nohi', echo=True)

async def main() :
    async with engine.connect() as conn:
        sql = "select id, name from t_user"
        result = await conn.execute(text(sql))
        print(result.all())

asyncio.run(main())