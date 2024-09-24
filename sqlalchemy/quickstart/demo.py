import asyncio
import contextlib

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.future import select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker


class _Base:
    __mapper_args__ = {"eager_defaults": True}
DemoBase = declarative_base(cls=_Base)

class Parent(DemoBase):
    __tablename__ = "demo_parent"
    id = Column(Integer, primary_key=True)
    data = Column(String(100))
    children = relationship("Child")

class Child(DemoBase):
    __tablename__ = "demo_child"
    id = Column(Integer, primary_key=True)
    parent_id = Column(ForeignKey("demo_parent.id"))

class UnitOfWorkFactory():
    def __init__(self, session_factory: sessionmaker):
        self._session_factory = session_factory

    @contextlib.asynccontextmanager
    async def __call__(self):
        uow = self._session_factory()
        try:
            yield uow
        finally:
            await uow.rollback()
            await uow.close()

async def async_main():
    print('===> create_async_engine')
    engine = create_async_engine(
        'mysql+asyncmy://root:root1234@127.0.0.1:3306/nohi',
        echo=True,
        future=True,
        pool_size=10,
        max_overflow=5,
        pool_timeout=5,
        pool_pre_ping=True,
    )
    print('===> engine.begin()')
    async with engine.begin() as conn:
        await conn.run_sync(DemoBase.metadata.drop_all)
        await conn.run_sync(DemoBase.metadata.create_all)

    print('===> sessionmaker')
    session_factory = sessionmaker(engine, class_=AsyncSession, future=True)

    print('===> uow_factory')
    uow_factory = UnitOfWorkFactory(session_factory)

    print('===> uow_factory')
    async with uow_factory() as uow:
        p = Parent(children=[Child()])
        p.data = 'init'
        uow.add(p)
        await uow.commit()

    print('===> 查询 and 更新')
    try:
        async with uow_factory() as uow:
            stmt = select(Parent).with_for_update(of=Parent)
            result = await uow.execute(stmt)
            print('===> 查询结束:', result)
            for item in result.scalars():
                print('===> item.data', item.id, item.data)
                item.data = "updated"
                # item.children # Raises sqlalchemy.exc.MissingGreenlet
            # await uow.commit
    except:
        print('===> sleep(5)')
        await asyncio.sleep(5)
        raise

print('===> before run')
asyncio.run(async_main())
print('===> after run')