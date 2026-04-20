from fastapi import FastAPI
import json

app = FastAPI()


def loader():
    with open("patients.json","r") as f:
        r = json.load(f)
        return r
    
@app.get("/")
def Home():
    return {"message":"Patient Data"}

@app.get("/About")
def About():
    return {"message":"A patient Data manager API"}

@app.get("/patients")
def Main():
    return loader()


