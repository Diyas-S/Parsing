import json
from fastapi import FastAPI

app = FastAPI()

with open("smartphones.json", "r") as file:
    smartphones_db = json.load(file)


@app.get("/smartphones")
async def get_smartphones_by_price(price: int):
    response = []
    for smartphone in smartphones_db:
        if smartphone['price'] == price:
            response.append(smartphone)

    return response
