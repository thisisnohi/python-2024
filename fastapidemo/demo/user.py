from datetime import date
import time
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 定义参数类
class User(BaseModel):
    id: int
    name: str
    joined: date


def testUser():
    my_user : User = User(id=3, name="John Doe", joined="2018-07-19")
    second_user_date = {
        "id": 4,
        "name": "Mary",
        "joined": "2018-11-30"
    }

    my_second_user: User = User(**second_user_date)

    print(str(my_user))
    print(str(my_second_user))

# testUser()

@app.get("/items/{item_id}")
async def read_item(item_id: int, q:str = None):
    print("Start : %s" % time.ctime());
    time.sleep( 5 )
    print("End : %s" % time.ctime())
    return User(id=3, name="John Doe", joined="2018-07-19")

@app.put("/items/{item_id}")
def read_item(item_id: int, item: User):
    return {"item_name": item.id, "item_id": item_id}



