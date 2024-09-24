from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from quickstart.model.User import User

engine = create_engine("mysql+pymysql://root:root1234@127.0.0.1:3306/nohi?charset=utf8")

# 删除数据 1，2，3
with engine.connect() as conn:
    sql = "delete from t_user where id in ('1','2','3')"
    conn.execute(text(sql))
    conn.commit()

with Session(engine) as session:
    user = User(id=1, user_code='1001', name='NOHI', telephone='18012920403', email='thisnohi@163.com', remark='11')
    session.add(user)
    session.commit()
    print('===> insert over')

with Session(engine) as session:
    user1 = User(id=2, user_code='1001', name='NOHI', telephone='18012920403', email='thisnohi@163.com', remark='11')
    user2 = User(id=3, user_code='1002', name='NOHI', telephone='18012920403', email='thisnohi@163.com', remark='11')

    session.add_all([user1, user2])
    session.commit()
    print('===> insert over')

with engine.connect() as conn:
    sql = "select * from t_user"
    result = conn.execute(text(sql))
    # print(result.all())
    for row in result:
        print(row)
