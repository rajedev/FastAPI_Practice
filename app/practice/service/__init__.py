"""
Public service API for the practice app.

Routers should import from ``app.practice.service``; implementation lives in
submodules such as ``products``.
"""

from app.practice.service.products import (
    ProductException,
    create_product,
    list_products,
    provide_product,
    provide_product_by_category,
    update_product
)
