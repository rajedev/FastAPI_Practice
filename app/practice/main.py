"""
Author: Rajendhiran Easu
Date: 06/01/26
Description: Main file to run the API server
"""

from fastapi import FastAPI

from app.practice.router import product_router, user_router

API_V1_PREFIX = "/api/v1"

app = FastAPI(
    title="Murugan Super Stores - Practice FastAPI",
    version="1.0.0",
    description="Versioned HTTP API. All route modules are mounted under `/api/v1`.",
    swagger_ui_parameters={"tryItOutEnabled":True}
)

#app.include_router(user_router, prefix=API_V1_PREFIX)
app.include_router(user_router)
app.include_router(product_router, prefix=API_V1_PREFIX)

# commented below and using
# `fastapi run app/practice/main.py` using fastapi[standard]
# `uvicorn app.practice.main:app --reload` using uvicorn

# if __name__ == "__main__":
#      import uvicorn
#      uvicorn.run(app=app)
#
#     uvicorn.run("app.practice.main:app", host="127.0.0.1", port=8000, reload=True)
