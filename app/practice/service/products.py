"""
Author: Rajendhiran Easu
Date: 20/04/26
Description:
"""

from pydantic import TypeAdapter

from app.practice.model.product_schema import Product, ProductPatch

__product_json = '[{"pid": "142ABC", "name": "Product A", "category": "Electronics", "description": "Product from the ABC", "price":200}, {"pid": "892JKN", "name": "Product B", "category": "Electronics", "description": "Product from the JKN", "price":134}, {"pid": "186KBN", "name": "Product C", "category": "Electronics", "description": "Product from the KBN", "price":86}, {"pid": "451LMN", "name": "Product D", "category": "Home Appliances", "description": "Product from the LMN", "price":320}, {"pid": "773QWE", "name": "Product E", "category": "Home Appliances", "description": "Product from the QWE", "price":158}, {"pid": "992RTY", "name": "Product F", "category": "Home Appliances", "description": "Product from the RTY", "price":410}, {"pid": "615UIO", "name": "Product G", "category": "Furniture", "description": "Product from the UIO", "price":275}, {"pid": "804PAS", "name": "Product H", "category": "Furniture", "description": "Product from the PAS", "price":192}, {"pid": "223DFG", "name": "Product I", "category": "Furniture", "description": "Product from the DFG", "price":150}, {"pid": "567HJK", "name": "Product J", "category": "Toys", "description": "Product from the HJK", "price":45}, {"pid": "334ZXC", "name": "Product K", "category": "Toys", "description": "Product from the ZXC", "price":60}, {"pid": "778VBN", "name": "Product L", "category": "Toys", "description": "Product from the VBN", "price":25}, {"pid": "901MKO", "name": "Product M", "category": "Electronics", "description": "Product from the MKO", "price":175}, {"pid": "129WER", "name": "Product N", "category": "Home Appliances", "description": "Product from the WER", "price":138}, {"pid": "665TYU", "name": "Product O", "category": "Furniture", "description": "Product from the TYU", "price":112}]'

__adapter = TypeAdapter(list[Product])
_products: list[Product] = __adapter.validate_json(__product_json)


class ProductException(Exception):
    def __init__(self, pid: str, msg: str) -> None:
        self.pid = pid
        super().__init__(msg)


def list_products(limit: int) -> list[Product]:
    return _products[:limit]


def provide_product(pid: str) -> Product | None:
    return next((product for product in _products if product.pid == pid), None)


def provide_product_by_category(
        category_name: str,
        limit: int | None,
) -> list[Product]:
    category_expected = category_name.strip().casefold()
    filtered = [
        product
        for product in _products
        if product.category.casefold() == category_expected
    ]
    return filtered if limit is None else filtered[:limit]


def create_product(product: Product) -> Product:
    if any(item.pid == product.pid for item in _products):
        raise ProductException(product.pid, f"Product with pid {product.pid} already exists")
    _products.append(product)
    return product

def update_product(pid: str, patch: ProductPatch) -> Product:
    data = patch.model_dump(exclude_unset=True)
    for i, item in enumerate(_products):
        if item.pid == pid:
            updated = item.model_copy(update=data)
            _products[i] = updated
            return updated
    raise ProductException(pid, f"Product with pid {pid} does not exist")
