"""
Author: Rajendhiran Easu
Date: 18/04/26
Description: Simple Product Info API methods for practicing fastapi
"""

from fastapi import FastAPI

app = FastAPI(title="Product Info")

products = [
    {
        "pid": "142ABC",
        "name": "Product A",
        "category": "Home Appliances",
        "description": "Product from the ABC",
        "price": 200
    },
    {
        "pid": "892JKN",
        "name": "Product B",
        "category": "Electronics",
        "description": "Product from the JKN",
        "price": 134
    },
    {
        "pid": "186KBN",
        "name": "Product C",
        "category": "Electronics",
        "description": "Product from the KBN",
        "price": 86
    }
]


@app.get("/products_list")
def products_list():
    return products


@app.get("/product/{pid}")
def get_product(pid: str):
    return next((product for product in products if product["pid"] == pid), None)


@app.get("/product/category/{category_name}")
def get_product_by_category(category_name: str):
    category_expected = category_name.strip().casefold()
    return [
        product
        for product in products
        if product["category"].casefold() == category_expected
    ]
