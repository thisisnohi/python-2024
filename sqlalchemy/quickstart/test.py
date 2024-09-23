import asyncio

from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine

from quickstart.model.User import Base


async def async_main():
    print('===>async_main')
    # 创建数据库引擎
    # echo=True 参数表示连接发出的 SQL 将被记录到标准输出。
    engine = create_async_engine(
        'mysql+asyncmy://root:root1234@127.0.0.1:3306/nohi',
        echo=True,
        future=True,
        pool_size=10,
        max_overflow=5,
        pool_timeout=5,
        pool_pre_ping=True,
    )

    async with engine.begin() as conn:
        print(conn.get_isolation_level())
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    # using another isolation level
    with engine.connect().execution_options(
            isolation_level="SERIALIZABLE"
    ) as conn:
        print(conn.get_isolation_level())  # SERIALIZABLE

    async with engine.connect() as conn:
        print(conn.get_isolation_level())  # REPEATABLE READ
        sql = "select id, name from t_user"
        result = await conn.execute(text(sql))
        print('==============')
        print(result.all())
        print('==============')


print("===> before run")
asyncio.run(async_main())
print("===> after run")

# with engine.connect() as con:
#     sql = 'select * from t_user'
#     rs = list(con.execute(sql))
#     print(rs)
