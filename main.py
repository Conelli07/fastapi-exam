from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Characteristics(BaseModel):
    max_speed: float
    max_fuel_capacity: float

class Car(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristics

cars: List[Car] = []

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/cars", status_code=201)
def create_car(car: Car):
    cars.append(car)
    return car

@app.get("/cars", response_model=List[Car])
def get_cars():
    return cars

@app.get("/cars/{id}", response_model=Car)
def get_car(id: str):
    for car in cars:
        if car.identifier == id:
            return car
    raise HTTPException(status_code=404, detail=f"Car with id {id} not found")


