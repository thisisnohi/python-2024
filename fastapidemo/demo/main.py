from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 定义参数类
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q, "code":'111'}


@app.put("/items/v2/{item_id}")
def read_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name}

# 运行方式
# main对应文件?   app对应 app = FastAPI()
# uvicorn main:app --reload