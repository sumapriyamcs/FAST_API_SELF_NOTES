# main.py
# Import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel


class CarModel(BaseModel):
    manufacturer: str
    modelName: str
    cc: int
    onRoadPrice: int


# Initialize the app
app = FastAPI()


# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Welcome to december"}


@app.post("/cars")
def add_car(car: CarModel):

    # add your code

    return car
