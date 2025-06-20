from fastapi import FastAPI

# Users App
app = FastAPI()

@app.get("/users/{name}")
def get_name(name: str):
    return {"user": {"name": name}}


# To run this, use the following command:
# uvicorn script5_app1:app --reload --port 8000

# Then you can access:
# curl http://127.0.0.1:8000/users/john