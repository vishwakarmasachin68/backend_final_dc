from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import models, schemas
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from datetime import date

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://dc-generator.onrender.com"],
    # allow_origins = ["*"],  # Allows all origins, adjust as needed 
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

@app.post("/clients/", response_model=schemas.ClientSchema)
def add_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    existing_client = db.query(models.Client).filter(models.Client.name == client.name).first()
    if existing_client:
        raise HTTPException(status_code=400, detail="Client already exists")

    db_client = models.Client(name=client.name)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client
        
# Location endpoints
@app.get("/locations/", response_model=List[schemas.LocationSchema])
def get_locations(db: Session = Depends(get_db)):
    return db.query(models.Location).all()

@app.post("/locations/", response_model=schemas.LocationSchema)
def add_location(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    existing_location = db.query(models.Location).filter(models.Location.name == location.name).first()
    if existing_location:
        raise HTTPException(status_code=400, detail="Location already exists")
    db_location = models.Location(name=location.name)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

# Project endpoints
@app.get("/projects/", response_model=List[schemas.ProjectSchema])
def get_projects(db: Session = Depends(get_db)):
    return db.query(models.Project).all()

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

@app.put("/challans/{id}/", response_model=schemas.ChallanSchema)
def update_challan(id: int, challan: schemas.ChallanSchema, db: Session = Depends(get_db)):
    # First get the existing challan
    db_challan = db.query(models.Challan).filter(models.Challan.id == id).first()
    if not db_challan:
        raise HTTPException(status_code=404, detail="Challan not found")
    
  
    challan_data = challan.dict(exclude={"items", "id"})

    for key, value in challan_data.items():
        setattr(db_challan, key, value)
    

    db.query(models.ChallanItem).filter(models.ChallanItem.challan_id == id).delete()
    
    
    for item in challan.items:
        db_item = models.ChallanItem(**item.dict(), challan_id=id)
        db.add(db_item)
    
    db.commit()
    db.refresh(db_challan)
    
   
    items = db.query(models.ChallanItem).filter(models.ChallanItem.challan_id == id).all()
    res = schemas.ChallanSchema.from_orm(db_challan)
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


@app.put("/challan-items/{item_id}/return")
def mark_item_as_returned(
    item_id: int, 
    returned_data: schemas.ItemReturnSchema, 
    db: Session = Depends(get_db)
):
    db_item = db.query(models.ChallanItem).filter(models.ChallanItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db_item.returned_date = returned_data.returned_date
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/assets/", response_model=List[schemas.AssetSchema])
def get_assets(db: Session = Depends(get_db)):
    return db.query(models.Asset).all()

@app.post("/assets/", response_model=schemas.AssetSchema)
def add_asset(asset: schemas.AssetCreate, db: Session = Depends(get_db)):
    existing_asset = db.query(models.Asset).filter(models.Asset.asset_id == asset.asset_id).first()
    if existing_asset:
        raise HTTPException(status_code=400, detail="Asset ID already exists")
    db_asset = models.Asset(**asset.dict())
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

@app.put("/assets/{asset_id}", response_model=schemas.AssetSchema)
def update_asset(asset_id: str, asset: schemas.AssetCreate, db: Session = Depends(get_db)):
    db_asset = db.query(models.Asset).filter(models.Asset.asset_id == asset_id).first()
    if not db_asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    for key, value in asset.dict().items():
        setattr(db_asset, key, value)
    db.commit()
    db.refresh(db_asset)
    return db_asset

@app.delete("/assets/{asset_id}")
def delete_asset(asset_id: str, db: Session = Depends(get_db)):
    db_asset = db.query(models.Asset).filter(models.Asset.asset_id == asset_id).first()
    if not db_asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    db.delete(db_asset)
    db.commit()
    return {"ok": True}