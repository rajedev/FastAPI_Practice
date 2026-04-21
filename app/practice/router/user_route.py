"""
Author: Rajendhiran Easu
Date: 18/04/26
Description: Simple Userinfo API methods
"""

from fastapi import APIRouter, HTTPException, Form

user_router = APIRouter(prefix="/users", tags=["users"])

user_id = [124, 123, 452]


@user_router.get("/welcome")
def initial():
    return {"message": "God Knows All, TIG"}


@user_router.get("/{uid}")
def user(uid: int):
    return {"is_user_active": uid in user_id}


@user_router.post(path="/raise_issue")
def raise_issue(uid: int = Form(...),
                  issue_description: str = Form(..., min_length=5, max_length=50)):
    is_user_exist = uid in user_id
    if is_user_exist:
        return {
            "message": f"Issue submitted by {uid} and Details:{issue_description}"
        }
    raise HTTPException(status_code=404, detail="User not exist")
