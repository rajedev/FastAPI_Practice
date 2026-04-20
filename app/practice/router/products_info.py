"""
Author: Rajendhiran Easu
Date: 18/04/26
Description: Product HTTP API (versioned under /api/v1 in main).
"""

from fastapi import APIRouter, HTTPException, Query

import app.practice.service as product_svc
from app.practice.model.product_schema import ErrorResponse, Product

product_router = APIRouter(prefix="/products", tags=["products"])


@product_router.get(
    "", # Explicit path is not required, it works with prefix
    response_model=list[Product],
    responses={
        422: {"description": "Invalid query parameters"},
    },
    summary="List products",
)
def list_products(limit: int = Query(ge=1)) -> list[Product]:
    return product_svc.list_products(limit)


@product_router.get(
    "/category/{category_name}",
    response_model=list[Product],
    responses={
        404: {"model": ErrorResponse, "description": "No products for this category"},
        422: {"description": "Invalid parameters"},
    },
    summary="List products in a category",
)
def get_products_by_category(
        category_name: str,
        limit: int | None = Query(default=None, ge=1),
) -> list[Product]:
    response_data = product_svc.provide_product_by_category(category_name, limit)
    if not response_data:
        raise HTTPException(status_code=404, detail="category does not exist")
    return response_data


@product_router.get(
    "/{pid}",
    name="get_product_by_pid",
    response_model=Product,
    responses={
        404: {"model": ErrorResponse, "description": "Product id not found"},
        422: {"description": "Invalid path or parameters"},
    },
    summary="Get one product by id",
)
def get_product(pid: str) -> Product:
    response_data = product_svc.provide_product(pid)
    if response_data is None:
        raise HTTPException(status_code=404, detail="pid does not exist")
    return response_data


@product_router.post(
    "/create",
    response_model=Product,
    responses={
        409: {"model": ErrorResponse, "description": "Product id already exists"},
        422: {"description": "Request body failed validation"},
    },
    summary="Create a new product",
)
def create_product(
        item: Product
) -> Product:
    try:
        return product_svc.create_product(item)
    except product_svc.ProductAlreadyExistsError:
        raise HTTPException(status_code=409, detail="Product already exists") from None
