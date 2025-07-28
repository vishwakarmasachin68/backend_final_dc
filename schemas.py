from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class ClientCreate(BaseModel):
    name: str

class LocationCreate(BaseModel):
    name: str

class ProjectCreate(BaseModel):
    client: str
    location: str
    has_po: str
    po_number: Optional[str] = None
    project_name: str
    project_details: Optional[str] = None
    field_supervisor: Optional[str] = None
    persons_involved: Optional[str] = None  # as JSON string
    
class ClientSchema(BaseModel):
    id: Optional[int]
    name: str
    class Config:
        orm_mode = True

class LocationSchema(BaseModel):
    id: Optional[int]
    name: str
    class Config:
        orm_mode = True

class ProjectSchema(BaseModel):
    id: Optional[int]
    client: str
    location: str
    has_po: str
    po_number: Optional[str]
    project_name: str
    project_details: Optional[str]
    field_supervisor: Optional[str]
    persons_involved: Optional[str]        # as JSON string
    class Config:
        orm_mode = True

class ChallanItemSchema(BaseModel):
    id: Optional[int]
    challan_id: Optional[int]
    sno: int
    asset_name: str
    description: Optional[str]
    quantity: int
    serial_no: Optional[str]
    returnable: str
    expected_return_date: Optional[date]
    returned_date: Optional[date]

    class Config:
        orm_mode = True
        

class ChallanSchema(BaseModel):
    id: Optional[int]
    dc_number: str
    dc_sequence: str
    date: date
    name: Optional[str]
    project_name: Optional[str]
    client: Optional[str]
    location: Optional[str]
    has_po: Optional[str]
    po_number: Optional[str]
    items: Optional[List[ChallanItemSchema]] = []

    class Config:
        orm_mode = True
