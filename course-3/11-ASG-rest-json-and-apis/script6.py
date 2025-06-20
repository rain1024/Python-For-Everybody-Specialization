from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

db = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if 0 <= item_id < len(db):
        return db[item_id]
    return {"error": "Item not found"}

@app.get("/items/")
def read_items():
    return db

@app.post("/items/")
def create_item(item: Item):
    db.append(item)
    return item

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
