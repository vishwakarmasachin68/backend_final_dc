from pydantic import BaseModel
from typing import Optional, List, Union
from datetime import date

# Category schemas
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategorySchema(CategoryBase):
    id: int

    class Config:
        orm_mode = True

# Client schemas
class ClientBase(BaseModel):
    name: str

class ClientCreate(ClientBase):
    pass

class ClientSchema(ClientBase):
    id: int

    class Config:
        orm_mode = True

# Location schemas
class LocationBase(BaseModel):
    name: str

class LocationCreate(LocationBase):
    pass

class LocationSchema(LocationBase):
    id: int

    class Config:
        orm_mode = True

# Project schemas
class ProjectBase(BaseModel):
    name: str
    client: str
    project_lead: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    status: Optional[str] = "active"

class ProjectCreate(ProjectBase):
    pass

class ProjectSchema(ProjectBase):
    id: int

    class Config:
        orm_mode = True

# Asset schemas
class AssetBase(BaseModel):
    asset_id: str
    asset_name: str
    category: str
    make: Optional[str] = None
    model: Optional[str] = None
    serial_number: str
    description: Optional[str] = None
    supplier_details: Optional[str] = None
    warranty_details: Optional[str] = None
    date_of_purchase: Optional[date] = None
    last_service_date: Optional[date] = None
    covered_under_amc: Optional[bool] = False
    amc_vendor_details: Optional[str] = None
    asset_issued_to: Optional[str] = None
    employee_number: Optional[str] = None
    date_of_issue: Optional[date] = None
    returned_date: Optional[date] = None
    condition: Optional[str] = None
    current_location: Optional[str] = None
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
    class Config:
        orm_mode = True

# Asset Tracking schemas
class AssetTrackingBase(BaseModel):
    asset_id: str
    transaction_type: str
    date: date
    from_location: Optional[str] = None
    to_location: Optional[str] = None
    issued_to: Optional[str] = None
    employee_number: Optional[str] = None
    return_date: Optional[date] = None
    remarks: Optional[str] = None

class AssetTrackingCreate(AssetTrackingBase):
    pass

class AssetTrackingSchema(AssetTrackingBase):
    id: int

    class Config:
        orm_mode = True

# Challan Item schemas
class ChallanItemBase(BaseModel):
    asset_id: Optional[str] = None
    description: str
    quantity: int
    expected_return_date: Optional[date] = None
    returned_date: Optional[date] = None

class ChallanItemCreate(ChallanItemBase):
    pass

class ChallanItemSchema(ChallanItemBase):
    id: int
    challan_id: int

    class Config:
        orm_mode = True

# Challan schemas
class ChallanBase(BaseModel):
    dc_number: Optional[str] = None
    date: date
    client: str
    project: str
    location: str
    has_po: str
    po_number: Optional[str] = None
    dc_sequence: int
    prepared_by: str
    approved_by: str
    received_by: Optional[str] = None
    items: List[ChallanItemCreate] = []

class ChallanCreate(ChallanBase):
    pass

class ChallanSchema(ChallanBase):
    id: int
    items: List[ChallanItemSchema] = []

    class Config:
        orm_mode = True