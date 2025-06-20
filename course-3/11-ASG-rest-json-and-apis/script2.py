from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# To run this, use the following command:
# uvicorn script2:app --reload

# Then run the following command:
# curl http://127.0.0.1:8000/