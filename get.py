from fastapi import FastAPI,Path
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
@app.get("/view/{patient_id}")
def view_patient(patient_id:int = Path(...,description="Id of the patient",example="1")):
    data = loader()
    for patient in data:
        if patient["id"] == patient_id:
            return patient
        return {"error":"cant fetch patient data"}


