"""
Author: Rajendhiran Easu
Date: 19/04/26
Description: Pydantic model for Product Info API methods for practicing fastapi
"""

from pydantic import BaseModel


class Products(BaseModel):
    """Product info API methods for practicing fastapi"""
    pid: str
    name: str
    category: str
    price: float


class ErrorResponse(BaseModel):
    """Default FastAPI / Starlette HTTPException JSON shape (string detail)."""
    detail: str
