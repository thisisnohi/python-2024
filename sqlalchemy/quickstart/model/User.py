import datetime
from typing import List

from sqlalchemy import String, DateTime, Integer, func, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "t_user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, comment='主键ID')
    create_datetime: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), comment='创建时间')
    update_datetime: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        comment='更新时间'
    )
    delete_datetime: Mapped[datetime] = mapped_column(DateTime, nullable=True, comment='删除时间')
    is_delete: Mapped[bool] = mapped_column(Boolean, default=False, comment="是否软删除")

    user_code: Mapped[str] = mapped_column(String(11), nullable=False, index=True, comment="用户编号", unique=False)
    name: Mapped[str] = mapped_column(String(50), index=True, nullable=False, comment="姓名")
    telephone: Mapped[str] = mapped_column(String(11), nullable=False, index=True, comment="手机号", unique=False)
    email: Mapped[str] = mapped_column(String(50), comment="邮箱地址")
    birthday: Mapped[datetime] = mapped_column(DateTime, nullable=True, comment="生日")
    age: Mapped[int] = mapped_column(Integer, nullable=True, comment="年龄")
    remark: Mapped[str] = mapped_column(String(1000), comment="备注")
    create_by: Mapped[str] = mapped_column(String(1000), comment="创建人")
    update_by: Mapped[str] = mapped_column(String(1000), comment="更新人")

    # 一对多关联
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str] = mapped_column(String(100), comment="邮箱")
    user_id: Mapped[int] = mapped_column(ForeignKey("t_user.id"))

    # 一对一关联
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
