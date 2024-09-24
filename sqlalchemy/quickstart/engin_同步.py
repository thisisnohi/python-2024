from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:root1234@127.0.0.1:3306/nohi?charset=utf8")

with engine.connect() as conn:
    sql = "select id, name from t_user"
    result = conn.execute(text(sql))
    print(result.all())
