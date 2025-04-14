from fastapi import FastAPI
from api.routers import chat

app = FastAPI()
app.include_router(chat.router, prefix="/api/v1/chat")

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
