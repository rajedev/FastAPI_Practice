"""
Author: Rajendhiran Easu
Date: 18/04/26
Description: Simple Userinfo API methods
"""

from fastapi import APIRouter

user_router = APIRouter(prefix="/users", tags=["users"])

user_id = [124, 123, 452]


@user_router.get("/welcome")
def initial():
    return {"message": "God Knows All, TIG"}


@user_router.get("/{uid}")
def user(uid: int):
    return {"is_user_active": uid in user_id}
