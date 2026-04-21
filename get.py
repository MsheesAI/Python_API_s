from fastapi import FastAPI,Path,Query,HTTPException
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
@app.get("/Sort")# query param
def sort_patients(sort_by:str = Query(...,description="sort on the basis of disease and gender"),order:str = Query("asc",description="sort in asc or desc order") ):
    valid = ["disease","gender"]
    if sort_by not in valid:
     raise HTTPException(status_code=400, detail=f"invalid field select from {valid}")
    if order not in ["asc","desc"]:
       raise HTTPException(status_code=400,detail="Invalid order select between asc and desc")
    data = loader()
    sort_order = True if order == "desc" else False
    sorted_data = sorted(data, key=lambda x: x.get(sort_by, ""), reverse=sort_order)
    return sorted_data
    


        



