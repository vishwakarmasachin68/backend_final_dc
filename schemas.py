from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime

# Add these new schemas for categories
class CategoryCreate(BaseModel):
    name: str

class CategorySchema(BaseModel):
    id: Optional[int] = None
    name: str
    
    class Config:
        from_attributes = True

class ClientCreate(BaseModel):
    name: str

class ClientSchema(BaseModel):
    id: Optional[int] = None
    name: str
    
    class Config:
        from_attributes = True

class LocationCreate(BaseModel):
    name: str

class LocationSchema(BaseModel):
    id: Optional[int] = None
    name: str
    
    class Config:
        from_attributes = True

class ProjectCreate(BaseModel):
    client: Optional[str] = None
    location: Optional[str] = None
    has_po: Optional[str] = "no"
    po_number: Optional[str] = None
    project_name: str
    project_details: Optional[str] = None
    field_supervisor: Optional[str] = None
    persons_involved: Optional[str] = None

class ProjectSchema(BaseModel):
    id: Optional[int] = None
    client: Optional[str] = None
    location: Optional[str] = None
    has_po: Optional[str] = "no"
    po_number: Optional[str] = None
    project_name: str
    project_details: Optional[str] = None
    field_supervisor: Optional[str] = None
    persons_involved: Optional[str] = None
    
    class Config:
        from_attributes = True

class AssetBase(BaseModel):
    asset_id: str
    asset_name: str
    category: Optional[str] = None
    make: Optional[str] = None
    model: Optional[str] = None
    serial_number: str
    description: Optional[str] = None
    supplier_details: Optional[str] = None
    date_of_purchase: Optional[date] = None
    warranty_details: Optional[str] = None
    last_service_date: Optional[date] = None
    covered_under_amc: Optional[bool] = False
    amc_vendor_details: Optional[str] = None
    transaction_type: Optional[str] = None
    transaction_date: Optional[date] = None
    vendor_sent_to: Optional[str] = None
    received_from: Optional[str] = None
    purpose: Optional[str] = None
    issued_by: Optional[str] = None
    received_by: Optional[str] = None
    asset_issued_to: Optional[str] = None
    employee_number: Optional[str] = None
    date_of_issue: Optional[date] = None
    expected_return_date: Optional[date] = None
    returned_date: Optional[date] = None
    current_location: Optional[str] = None
    condition: Optional[str] = None
    status: Optional[str] = "available"
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

class AssetTrackingBase(BaseModel):
    asset_id: str
    asset_name: str
    serial_number: Optional[str] = None
    date: date
    transaction_type: str
    vendor_sent_to: Optional[str] = None
    received_from: Optional[str] = None
    purpose: Optional[str] = None
    issued_by: Optional[str] = None
    received_by: Optional[str] = None
    return_date: Optional[date] = None
    notes: Optional[str] = None

class AssetTrackingCreate(AssetTrackingBase):
    pass

class AssetTrackingSchema(AssetTrackingBase):
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class ChallanItemSchema(BaseModel):
    id: Optional[int] = None
    sno: int
    asset_id: Optional[str] = None
    asset_name: str
    description: Optional[str] = None
    quantity: int
    serial_no: Optional[str] = None
    returnable: str
    expected_return_date: Optional[date] = None
    returned_date: Optional[date] = None
    
    class Config:
        from_attributes = True

class ChallanBase(BaseModel):
    dc_sequence: str
    date: date
    name: Optional[str] = None
    project_name: Optional[str] = None
    client: Optional[str] = None
    location: Optional[str] = None
    has_po: Optional[str] = "no"
    po_number: Optional[str] = None
    items: List[ChallanItemSchema] = []

class ChallanCreate(ChallanBase):
    pass

class ChallanSchema(ChallanBase):
    id: Optional[int] = None
    dc_number: Optional[str] = None
    
    class Config:
        from_attributes = True

class ItemReturnSchema(BaseModel):
    returned_date: date