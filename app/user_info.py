"""
Author: Rajendhiran Easu
Date: 18/04/26
Description: Simple Userinfo API methods
"""

from fastapi import FastAPI

app = FastAPI(title="Employee App")

user_id = [124, 123, 452]

@app.get("/welcome")
def initial():
    return {"message": "God Knows All, I Trust in God"}


@app.get("/user/{uid}")
def user(uid: int):
    return {"is_user_active": uid in user_id}