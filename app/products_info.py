"""
Author: Rajendhiran Easu
Date: 18/04/26
Description: Simple Product Info API methods for practicing fastapi
"""

from typing import List

from fastapi import FastAPI, HTTPException, Query
from pydantic import TypeAdapter

from app.schemas import ErrorResponse, Products

app = FastAPI(title="Product Info")

product_json = '[{"pid": "142ABC", "name": "Product A", "category": "Electronics", "description": "Product from the ABC", "price":200}, {"pid": "892JKN", "name": "Product B", "category": "Electronics", "description": "Product from the JKN", "price":134}, {"pid": "186KBN", "name": "Product C", "category": "Electronics", "description": "Product from the KBN", "price":86}, {"pid": "451LMN", "name": "Product D", "category": "Home Appliances", "description": "Product from the LMN", "price":320}, {"pid": "773QWE", "name": "Product E", "category": "Home Appliances", "description": "Product from the QWE", "price":158}, {"pid": "992RTY", "name": "Product F", "category": "Home Appliances", "description": "Product from the RTY", "price":410}, {"pid": "615UIO", "name": "Product G", "category": "Furniture", "description": "Product from the UIO", "price":275}, {"pid": "804PAS", "name": "Product H", "category": "Furniture", "description": "Product from the PAS", "price":192}, {"pid": "223DFG", "name": "Product I", "category": "Furniture", "description": "Product from the DFG", "price":150}, {"pid": "567HJK", "name": "Product J", "category": "Toys", "description": "Product from the HJK", "price":45}, {"pid": "334ZXC", "name": "Product K", "category": "Toys", "description": "Product from the ZXC", "price":60}, {"pid": "778VBN", "name": "Product L", "category": "Toys", "description": "Product from the VBN", "price":25}, {"pid": "901MKO", "name": "Product M", "category": "Electronics", "description": "Product from the MKO", "price":175}, {"pid": "129WER", "name": "Product N", "category": "Home Appliances", "description": "Product from the WER", "price":138}, {"pid": "665TYU", "name": "Product O", "category": "Furniture", "description": "Product from the TYU", "price":112}]'

adapter = TypeAdapter(List[Products])
products: list[Products] = adapter.validate_json(product_json)


@app.get(
    "/product_list",
    response_model=list[Products],
    responses={
        422: {"description": "Invalid query parameters"},
    },
    summary="List products up to a limit",
)
def product_list(limit: int = Query(ge=1)) -> list[Products]:
    return products[:limit]


@app.get(
    "/product/{pid}",
    # response_model=Products, #optional to set this here, it infers from return type
    responses={
        404: {"model": ErrorResponse, "description": "Product id not found"},
        422: {"description": "Invalid path or parameters"},
    },
    summary="Get one product by id",
)
def get_product(pid: str) -> Products:
    response_data = next((product for product in products if product.pid == pid), None)
    if response_data is None:
        raise HTTPException(status_code=404, detail="pid does not exist")
    return response_data


@app.get(
    "/product/category/{category_name}",
    response_model=list[Products],
    responses={
        404: {"model": ErrorResponse, "description": "No products for this category"},
        422: {"description": "Invalid parameters"},
    },
    summary="List products in a category",
)
def get_product_by_category(
        category_name: str,
        limit: int | None = Query(default=None, ge=1),
) -> list[Products]:
    category_expected = category_name.strip().casefold()
    filtered = [
        product
        for product in products
        if product.category.casefold() == category_expected
    ]
    response_data = filtered if limit is None else filtered[:limit]
    if not response_data:
        raise HTTPException(status_code=404, detail="category does not exist")
    return response_data


@app.post(
    "/add_product",
    response_model=Products,
    responses={
        409: {"model": ErrorResponse, "description": "Product id already exists"},
        422: {"description": "Request body failed validation"},
    },
    summary="Create a new product",
)
def create_product(prod: Products) -> Products:
    if any(item.pid == prod.pid for item in products):
        raise HTTPException(status_code=409, detail="Product already exists")
    products.append(prod)
    return prod
