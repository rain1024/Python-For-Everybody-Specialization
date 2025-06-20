from fastapi import FastAPI
import random
# Users App
app = FastAPI()

@app.get("/orders/{order_id}")
def get_name(order_id: str):
    items = ["book", "pen", "pencil"]
    return {"order": {"order_id": order_id, "items": random.choice(items)}}


# To run this, use the following command:
# uvicorn script5_app2:app --reload --port 8001

# Then you can access:
# curl http://127.0.0.1:8001/orders/1