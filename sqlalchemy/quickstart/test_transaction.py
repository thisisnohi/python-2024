import asyncio

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

# 创建数据库引擎
# echo=True 参数表示连接发出的 SQL 将被记录到标准输出。
# asyncmy 为异步连接驱动
engine = create_async_engine(
    'mysql+asyncmy://root:root1234@127.0.0.1:3306/nohi',
    echo=True,
    future=True,
    pool_size=10,
    max_overflow=5,
    pool_timeout=5,
    pool_pre_ping=True,
)


async def get_all_date(conn):
    # 获取所有数据
    sql = "select * from demo_parent"
    result = await conn.execute(text(sql))
    for row in result:
        print(row.id, row.data)


# 测试事务
async def test_transaction():
    print('===>test_transaction')

    async with engine.begin() as conn:
        # REPEATABLE READ
        print("===> engine.begin() get_isolation_level ", await conn.get_isolation_level())

        await get_all_date(conn)

        # 清理历史数据
        print("===> 清理数据")
        sql = "delete from demo_parent where id in ('3','4')"
        result = await conn.execute(text(sql))
        print(result)

        # 查询数据
        await get_all_date(conn)

    # 设置隔离级别
    #  async with engine.connect().execution_options(
    #       isolation_level = "SERIALIZABLE"
    # )  会出现以下错误
    # TypeError: 'coroutine' object does not support the asynchronous context manager protocol
    async with engine.execution_options(
            isolation_level="SERIALIZABLE"
    ).connect() as conn:
        # SERIALIZABLE
        print("===> engine.begin() get_isolation_level ", await conn.get_isolation_level())

    # 测试事务，engine.connect() 默认事务不提交
    await connect_without_commit()
    # 测试事务，engine.connect() connect.commit 提交事务
    await connect_with_commit()
    # 测试事务 engine.begin 默认带事务
    await begin_with_commit()


async def connect_without_commit():
    # 测试事务
    # 默认不提交事务，直到遇到connection.commit
    async with engine.connect() as conn:
        # REPEATABLE READ
        print("===> engine.begin() get_isolation_level ", await conn.get_isolation_level())
        sql = "INSERT INTO demo_parent (id, data) VALUES (3, '测试事务connect_without_commit')"
        result = await conn.execute(text(sql))
        print("===> insert", result)

        # 查询
        await get_all_date(conn)

    print("===> connect_without_commit")
    # 查询
    async with engine.connect() as conn:
        await get_all_date(conn)

async def connect_with_commit():
    # 测试事务
    # connection.commit 提交事务
    async with engine.connect() as conn:
        # REPEATABLE READ
        print("===> engine.begin() get_isolation_level ", await conn.get_isolation_level())
        sql = "INSERT INTO demo_parent (id, data) VALUES (3, '测试事务connect_with_commit')"
        result = await conn.execute(text(sql))
        print("===> insert", result)

        # 查询
        await get_all_date(conn)
        # 提交事务
        await conn.commit()

    print("===> connect_with_commit")
    # 查询
    async with engine.connect() as conn:
        await get_all_date(conn)

async def begin_with_commit():
    # 测试事务
    # connection.commit 提交事务
    async with engine.begin() as conn:
        # REPEATABLE READ
        print("===> engine.begin() get_isolation_level ", await conn.get_isolation_level())
        sql = "INSERT INTO demo_parent (id, data) VALUES (4, '测试事务 begin_with_commit')"
        result = await conn.execute(text(sql))
        print("===> insert", result)
        # 查询
        await get_all_date(conn)




    print("===> begin_with_commit")
    # 查询
    async with engine.connect() as conn:
        await get_all_date(conn)

print("===> before run")
asyncio.run(test_transaction())
print("===> after run")
