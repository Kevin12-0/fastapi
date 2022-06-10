from fastapi import FastAPI

import sqlite3
from typing import List


app = FastAPI()


@app.get("/")
def Index():
    return {"message": 36.81}


