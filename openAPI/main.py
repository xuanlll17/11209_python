from typing import Union
from fastapi import FastAPI
import redis
import os
from dotenv import load_dotenv

load_dotenv()  # 載入.env的環境變數
# 連線到redis
redis_conn = redis.Redis.from_url(
    os.environ.get("REDIS_HOST_PASSWORD")
)  # 抓電腦的環境變數(REDIS_HOST_PASSWORD)

app = FastAPI()

# server提供了兩個get @app.get("/") @app.get("/items/{item_id}")
@app.get("/") 
def read_root():
    counter = redis_conn.incr('test:increment',1) # 建立redis的key(test:increment)裡面的值每次加一 # 每次執行加一(計數器) # 變數(counter)接收
    return {"Counter": counter} # key("Counter"),值(counter)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None): # q -> query(不在路徑裡)(選填)
    return {"item_id": item_id, "q": q}

# 執行main.py -> 終端機 uvicorn main(main.py):app(main.py裡面的app) --reload(開發環境下須打)
