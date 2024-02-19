from typing import Union

from fastapi import FastAPI

app = FastAPI()

# server提供了兩個get @app.get("/") @app.get("/items/{item_id}")
@app.get("/") 
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None): # q -> query(不在路徑裡)(選填)
    return {"item_id": item_id, "q": q}

# 執行main.py -> 終端機 uvicorn main(main.py):app(main.py裡面的app) --reload(開發環境下須打)
