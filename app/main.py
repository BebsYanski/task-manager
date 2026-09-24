"""Main Page"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    """Entry Point"""
    return {"message": "Welcome to Task manager"}
