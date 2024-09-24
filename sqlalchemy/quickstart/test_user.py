import asyncio

from sqlalchemy import delete, select, text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from quickstart.model.User import User

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

# 同步session
# Session = sessionmaker(engine)
# 异步session
Session = sessionmaker(bind=engine,class_=AsyncSession)

#
user = User()

async def init():
    await asyncio.sleep(1)
    # 初始化表结构
    # Base.metadata.create_all(engine)

    # 清理数据
    # 删除 11数据
    async with Session() as session:
        async with session.begin():
            await session.execute(delete(User).where(User.id == 11))
            await session.execute(text("delete from t_user where id in (12, 13)"))


    # 初始化数据
    async with Session() as session:
        async with session.begin():
            session.add(User(id=11, user_code='1001', name='NOHI', telephone='18012920403', email='thisnohi@163.com', remark='11'))

            user1 = User(id=12, user_code='1001', name='NOHI', telephone='18012920403', email='thisnohi@163.com',
                         remark='11')
            user2 = User(id=13, user_code='1002', name='NOHI', telephone='18012920403', email='thisnohi@163.com',
                         remark='11')
            session.add_all([user1, user2])

        sql = select(User).where(User.id.in_([11,12,13]))
        print("===> sql:", sql)
        result = await session.execute(sql)
        # print(result.all())
        # 必须使用 result.unique() ，否则报错：
        # sqlalchemy.exc.InvalidRequestError: The unique() method must be invoked on this Result, as it contains results that include joined eager loads against collections
        for row in result.unique().all():
            print(row)

async def user_model():
    print('===>user_model')
    await init()

asyncio.run(user_model())
