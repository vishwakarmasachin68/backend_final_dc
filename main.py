from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import models, schemas

from typing import List
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Allow CORS for frontend (adjust as per your host/port)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev only; set to your frontend origin in prod!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Client endpoints
@app.get("/clients/", response_model=List[schemas.ClientSchema])
def get_clients(db: Session = Depends(get_db)):
    return db.query(models.Client).all()

# @app.post("/clients/", response_model=schemas.ClientSchema)
# def add_client(client: schemas.ClientSchema, db: Session = Depends(get_db)):
#     db_client = models.Client(name=client.name)
#     db.add(db_client)
#     db.commit()
#     db.refresh(db_client)
#     return db_client

@app.post("/clients/", response_model=schemas.ClientSchema)
def add_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    db_client = models.Client(name=client.name)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


# Location endpoints
@app.get("/locations/", response_model=List[schemas.LocationSchema])
def get_locations(db: Session = Depends(get_db)):
    return db.query(models.Location).all()

# @app.post("/locations/", response_model=schemas.LocationSchema)
# def add_location(location: schemas.LocationSchema, db: Session = Depends(get_db)):
#     db_location = models.Location(name=location.name)
#     db.add(db_location)
#     db.commit()
#     db.refresh(db_location)
#     return db_location
@app.post("/locations/", response_model=schemas.LocationSchema)
def add_location(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    db_location = models.Location(name=location.name)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

# Project endpoints
@app.get("/projects/", response_model=List[schemas.ProjectSchema])
def get_projects(db: Session = Depends(get_db)):
    return db.query(models.Project).all()

# @app.post("/projects/", response_model=schemas.ProjectSchema)
# def add_project(project: schemas.ProjectSchema, db: Session = Depends(get_db)):
#     db_project = models.Project(**project.dict())
#     db.add(db_project)
#     db.commit()
#     db.refresh(db_project)
#     return db_project

@app.post("/projects/", response_model=schemas.ProjectSchema)
def add_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = models.Project(**{k: project.dict()[k] for k in project.dict() if k != "persons_involved"})
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@app.put("/projects/{id}/", response_model=schemas.ProjectSchema)
def update_project(id: int, project: schemas.ProjectSchema, db: Session = Depends(get_db)):
    db_project = db.query(models.Project).filter(models.Project.id == id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    for var, value in project.dict().items():
        setattr(db_project, var, value)
    db.commit()
    db.refresh(db_project)
    return db_project

@app.delete("/projects/{id}/")
def delete_project(id: int, db: Session = Depends(get_db)):
    db_project = db.query(models.Project).filter(models.Project.id == id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(db_project)
    db.commit()
    return {"ok": True}

# Challan endpoints
@app.get("/challans/", response_model=List[schemas.ChallanSchema])
def get_challans(db: Session = Depends(get_db)):
    challans = db.query(models.Challan).all()
    result = []
    for c in challans:
        items = db.query(models.ChallanItem).filter(models.ChallanItem.challan_id == c.id).all()
        c_data = schemas.ChallanSchema.from_orm(c)
        c_data.items = items
        result.append(c_data)
    return result

@app.post("/challans/", response_model=schemas.ChallanSchema)
def add_challan(challan: schemas.ChallanSchema, db: Session = Depends(get_db)):
    
    c = models.Challan(**{k: challan.dict()[k] for k in challan.dict() if k != "items"})
    db.add(c)
    db.flush()  # to get ID
    # print("Payload received at /challans/:", challan.dict())

    # Add items
    for item in challan.items:
        db_item = models.ChallanItem(**item.dict(), challan_id=c.id)
        db.add(db_item)
    db.commit()
    db.refresh(c)
    items = db.query(models.ChallanItem).filter(models.ChallanItem.challan_id == c.id).all()
    res = schemas.ChallanSchema.from_orm(c)
    res.items = items
    return res

@app.delete("/challans/{id}/")
def delete_challan(id: int, db: Session = Depends(get_db)):
    c = db.query(models.Challan).filter(models.Challan.id == id).first()
    db.query(models.ChallanItem).filter(models.ChallanItem.challan_id == id).delete()
    if c:
        db.delete(c)
        db.commit()
    return {"ok": True}

@app.delete("/clients/{client_name}")
def delete_client(client_name: str, db: Session = Depends(get_db)):
    db_client = db.query(models.Client).filter(models.Client.name == client_name).first()
    if not db_client:
        raise HTTPException(status_code=404, detail="Client not found")
    db.delete(db_client)
    db.commit()
    return {"message": "Client deleted successfully"}

@app.delete("/locations/{location_name}")
def delete_location(location_name: str, db: Session = Depends(get_db)):
    db_location = db.query(models.Location).filter(models.Location.name == location_name).first()
    if not db_location:
        raise HTTPException(status_code=404, detail="Location not found")
    db.delete(db_location)
    db.commit()
    return {"message": "Location deleted successfully"}