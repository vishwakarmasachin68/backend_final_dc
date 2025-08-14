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
    persons_involved: Optional[str] = None  
    
class ClientSchema(BaseModel):
    id: Optional[int]
    name: str
    class Config:
        from_attributes = True

class LocationSchema(BaseModel):
    id: Optional[int]
    name: str
    class Config:
        from_attributes = True

class ProjectSchema(BaseModel):
    id: Optional[int]
    client: str
    location: str
    has_po: str
    po_number: Optional[str]
    project_name: str
    project_details: Optional[str]
    field_supervisor: Optional[str]
    persons_involved: Optional[str]       
    class Config:
        from_attributes = True

class ChallanItemSchema(BaseModel):
    id: Optional[int] = None
    sno: int
    asset_name: str
    description: Optional[str]
    quantity: int
    serial_no: Optional[str]
    returnable: str
    expected_return_date: Optional[date]
    returned_date: Optional[date] = None

class ChallanSchema(BaseModel):
    id: Optional[int] = None
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
        from_attributes = True


class ItemReturnSchema(BaseModel):
    returned_date: date = date.today()

class AssetBase(BaseModel):
    asset_id: str
    asset_name: str
    category: Optional[str] = None
    make_model: Optional[str] = None
    serial_number: str
    supplier_details: Optional[str] = None
    date_of_purchase: Optional[date] = None
    warranty_details: Optional[str] = None
    last_service_date: Optional[date] = None
    covered_under_amc: Optional[bool] = False
    amc_vendor_details: Optional[str] = None
    condition: Optional[str] = None
    status: Optional[str] = "active"
    
    # Transaction fields
    transaction_date: Optional[date] = None
    transaction_type: Optional[str] = None  # inward/outward
    received_from: Optional[str] = None
    purpose: Optional[str] = None
    issued_by: Optional[str] = None
    received_by: Optional[str] = None
    expected_return_date: Optional[date] = None
    returned_date: Optional[date] = None
    is_received: Optional[bool] = False
    
    # Disposal fields
    disposal_approvals_obtained: Optional[bool] = False
    date_of_approval: Optional[date] = None
    approved_by: Optional[str] = None
    media_sanitised: Optional[bool] = False
    media_sanitised_by: Optional[str] = None
    date_of_media_sanitisation: Optional[date] = None

class AssetCreate(AssetBase):
    pass

class AssetSchema(AssetBase):
    id: Optional[int] = None
    
    class Config:
        from_attributes = True