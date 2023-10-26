from fastapi import FastAPI

# 默认端口8000
#启动命令 uvicorn web:app --reload
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

