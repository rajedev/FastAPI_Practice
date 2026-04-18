"""
Author: Rajendhiran Easu
Date: 06/01/26
Description: Main file to run the API server
"""
import uvicorn

if __name__ == "__main__":
    #uvicorn.run("app.user_info:app", host="127.0.0.1", port=8000, reload=True)
    uvicorn.run("app.products_info:app", host="127.0.0.1", port=8000, reload=True)
