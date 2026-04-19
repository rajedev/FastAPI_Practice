"""
Author: Rajendhiran Easu
Date: 18/04/26
Description: Simple Product Info API methods for practicing fastapi
"""

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Product Info")

products = [{"pid":"142ABC","name":"Product A","category":"Electronics","description":"Product from the ABC","price":200},{"pid":"892JKN","name":"Product B","category":"Electronics","description":"Product from the JKN","price":134},{"pid":"186KBN","name":"Product C","category":"Electronics","description":"Product from the KBN","price":86},{"pid":"451LMN","name":"Product D","category":"Home Appliances","description":"Product from the LMN","price":320},{"pid":"773QWE","name":"Product E","category":"Home Appliances","description":"Product from the QWE","price":158},{"pid":"992RTY","name":"Product F","category":"Home Appliances","description":"Product from the RTY","price":410},{"pid":"615UIO","name":"Product G","category":"Furniture","description":"Product from the UIO","price":275},{"pid":"804PAS","name":"Product H","category":"Furniture","description":"Product from the PAS","price":192},{"pid":"223DFG","name":"Product I","category":"Furniture","description":"Product from the DFG","price":150},{"pid":"567HJK","name":"Product J","category":"Toys","description":"Product from the HJK","price":45},{"pid":"334ZXC","name":"Product K","category":"Toys","description":"Product from the ZXC","price":60},{"pid":"778VBN","name":"Product L","category":"Toys","description":"Product from the VBN","price":25},{"pid":"901MKO","name":"Product M","category":"Electronics","description":"Product from the MKO","price":175},{"pid":"129WER","name":"Product N","category":"Home Appliances","description":"Product from the WER","price":138},{"pid":"665TYU","name":"Product O","category":"Furniture","description":"Product from the TYU","price":112}]


@app.get("/product_list")
def product_list(limit: int):
    try:
        return products[:limit]
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Exception {e}")


@app.get("/product/{pid}")
def get_product(pid: str):
    response_data = next((product for product in products if product["pid"] == pid), None)
    if response_data:
        return response_data
    raise HTTPException(status_code=404, detail="pid is not exist")


@app.get("/product/category/{category_name}")
def get_product_by_category(category_name: str, limit: int = None):
    category_expected = category_name.strip().casefold()
    response_data= [
        product
        for product in products
        if product["category"].casefold() == category_expected
    ][:limit]
    if response_data:
        return response_data
    raise HTTPException(status_code=404, detail="category is not exist")
