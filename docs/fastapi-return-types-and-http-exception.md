# FastAPI: return types, `response_model`, and `HTTPException`

A short note on how **success** (typed returns) and **errors** (`HTTPException`) fit together—using a **list** of `Products` (filtered by **category**) and a **single** `Product` (looked up by **pid**).

---

## The idea in one paragraph

- **`-> list[Products]`** or **`-> Products`** describes what you **`return` when the request succeeds** (usually HTTP 200).
- **`raise HTTPException(status_code=404, detail="...")`** stops the handler and sends a **4xx** response with `{"detail": "..."}`. A **raise** is not a **return**, so it does not clash with your success type.
- **`response_model`** documents and serializes the **2xx** body; it does not replace error handling.

---

## One self-contained example

Everything below is a **single** copy-paste-friendly script: one `FastAPI` app, one `Products` model, one in-memory list, and **two URL patterns** shown in the same file (this is **not** about `APIRouter`—here everything is registered on one `app`). **Both** operations use `HTTPException` when nothing matches.

1. **List by category** — returns `list[Products]`; **404** if there are no products in that category.  
2. **Get by `pid`** — returns `Products`; **404** if that id does not exist.

```python
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI()


class Products(BaseModel):
    pid: str
    name: str
    category: str
    price: float


products: list[Products] = [
    Products(pid="p1", name="Item A", category="Electronics", price=99.0),
    Products(pid="p2", name="Item B", category="Electronics", price=49.0),
    Products(pid="p3", name="Item C", category="Toys", price=19.0),
]


@app.get("/products/category/{category_name}", response_model=list[Products])
def get_products_by_category(
    category_name: str,
    limit: int | None = Query(default=None, ge=1),
) -> list[Products]:
    want = category_name.strip().casefold()
    filtered = [p for p in products if p.category.casefold() == want]
    out = filtered if limit is None else filtered[:limit]
    if not out:
        raise HTTPException(
            status_code=404,
            detail="No products in this category",
        )
    return out


@app.get("/products/{pid}", response_model=Products)
def get_product_by_pid(pid: str) -> Products:
    found = next((p for p in products if p.pid == pid), None)
    if found is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return found
```

**Path shapes:** the URL that contains the fixed segment `…/category/…` is not the same as `…/products/{pid}`, so FastAPI can match the right operation without extra wiring.

---

## Quick reference

| Concept | In the example |
|--------|-----------------|
| `-> list[Products]` / `-> Products` | Type of the value on **success** (normal `return`). |
| `response_model=...` | Serializes the **2xx** body and drives OpenAPI for the success shape. |
| `HTTPException` | **Not found** (or other **4xx**): no fake product(s), no 200 with an “error” body. |

---

## Takeaway

Use the same pattern in each handler: after you load or query data, **`raise HTTPException`** when the rule says “not found,” otherwise **`return`** a **list** or a **single** model. The return type always describes the **happy path** only.

---

## LinkedIn (generic) — copy as needed

> In FastAPI, **return type** and **response_model** describe the **success** body: a single Pydantic model, or a list of that model—whatever the handler returns on a normal 2xx.
>
> When a lookup fails or a rule is broken, you **`raise HTTPException`** so the client gets a proper **4xx** status and a **detail** payload. That is separate from the return type, because **raise** is not **return**.
>
> **response_model** defines how the **success** response is built and documented; **HTTPException** is how you answer with an **error** without faking a 200.

**Hashtags (paste below the post, one line):**

```
#FastAPI #Python #API #BackendDevelopment #WebDevelopment #SoftwareEngineering #Pydantic #OpenAPI
```

---

*Swap in your own model names and paths as needed when you share the article.*
