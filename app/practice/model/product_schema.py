"""
Author: Rajendhiran Easu
Date: 19/04/26
Description: Pydantic models for the Product API
"""

from pydantic import BaseModel, Field


class Product(BaseModel):
    """Product info API methods for practicing fastapi"""
    pid: str = Field(min_length=1, description="Product ID")
    name: str
    category: str
    description: str
    price: float


class ProductPatch(BaseModel):
    """Partial update: only fields present in the JSON body are applied."""

    name: str | None = None
    category: str | None = None
    description: str | None = None
    price: float | None = None


class ErrorResponse(BaseModel):
    """Default FastAPI / Starlette HTTPException JSON shape (string detail)."""
    detail: str
