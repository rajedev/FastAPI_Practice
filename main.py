"""
Author: Rajendhiran Easu
Date: 06/01/26
Description: 
"""
from fastapi import FastAPI

app = FastAPI(title="Employee App")

user_id = [124, 123, 452]


@app.get("/welcome")
def users():
    return {"message": "God Knows All, I Trust in God"}


@app.get("/user")
def users(uid: int):
    is_user_active: bool = False
    if uid in user_id:
        is_user_active = True
    return {"is_user_active": is_user_active}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000)
