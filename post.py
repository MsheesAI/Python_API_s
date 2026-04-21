from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
import json
from typing import Literal,Annotated

app = FastAPI()

@app.get("/")
def hello():
    return {"message":"welcome to post req"}

class patient(BaseModel):
    id:Annotated[int,Field(...,description="Id of the patient")]
    name:Annotated[str,Field(...,description="name of the patient")]
    admitted:Annotated[bool,Field(...,description="Is Patient admitted")]
    age:Annotated[int,Field(...,description="Age of the patient")]
    gender:Annotated[Literal["Male","Female"],Field(...,description="Gender of the patient")]
    disease:Annotated[str,Field(...,description="disease of the patient")]

def loader():
    with open("patients.json","r") as f:
        data = json.load(f)
        return data
def save(data):
      with open("patients.json","w") as f:
        json.dump(data,f)

@app.post("/create",responses={
    400: {"description": "Patient already exists"},
    201: {"description": "Patient created successfully"}
})
def create_patient(Patient: patient):
    data = loader()

    # check if patient already exists
    for p in data:
        if p["id"] == Patient.id:
            raise HTTPException(status_code=400, detail="Patient already exists")

    # add new patient
    data.append(Patient.model_dump())

    save(data)

    return JSONResponse(status_code=201, content={"message": "Patient created successfully"}) 