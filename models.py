from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Date, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


# Add this new model for categories
class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    client = Column(String, nullable=True)
    location = Column(String, nullable=True)
    has_po = Column(String(10), default="no")
    po_number = Column(String, nullable=True)
    project_name = Column(String, nullable=False)
    project_details = Column(Text, nullable=True)
    field_supervisor = Column(String, nullable=True)
    persons_involved = Column(Text, nullable=True)

class Asset(Base):
    __tablename__ = "assets"
    
    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(String, unique=True, nullable=False)
    asset_name = Column(String, nullable=False)
    category = Column(String, nullable=True)  # This will now reference category names
    make = Column(String, nullable=True)
    model = Column(String, nullable=True)
    serial_number = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=True)
    supplier_details = Column(Text, nullable=True)
    date_of_purchase = Column(Date, nullable=True)
    warranty_details = Column(Text, nullable=True)
    last_service_date = Column(Date, nullable=True)
    covered_under_amc = Column(Boolean, default=False)
    amc_vendor_details = Column(Text, nullable=True)
    transaction_type = Column(String, nullable=True)
    transaction_date = Column(Date, nullable=True)
    vendor_sent_to = Column(String, nullable=True)
    received_from = Column(String, nullable=True)
    purpose = Column(String, nullable=True)
    issued_by = Column(String, nullable=True)
    received_by = Column(String, nullable=True)
    asset_issued_to = Column(String, nullable=True)
    employee_number = Column(String, nullable=True)
    date_of_issue = Column(Date, nullable=True)
    expected_return_date = Column(Date, nullable=True)
    returned_date = Column(Date, nullable=True)
    current_location = Column(String, nullable=True)
    condition = Column(String, nullable=True)
    status = Column(String, default="available")
    disposal_approvals_obtained = Column(Boolean, default=False)
    date_of_approval = Column(Date, nullable=True)
    approved_by = Column(String, nullable=True)
    media_sanitised = Column(Boolean, default=False)
    media_sanitised_by = Column(String, nullable=True)
    date_of_media_sanitisation = Column(Date, nullable=True)

class AssetTracking(Base):
    __tablename__ = "asset_tracking"
    
    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(String, nullable=False)
    asset_name = Column(String, nullable=False)
    serial_number = Column(String, nullable=True)
    date = Column(Date, nullable=False)
    transaction_type = Column(String, nullable=False)
    vendor_sent_to = Column(String, nullable=True)
    received_from = Column(String, nullable=True)
    purpose = Column(String, nullable=True)
    issued_by = Column(String, nullable=True)
    received_by = Column(String, nullable=True)
    return_date = Column(Date, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())

class Challan(Base):
    __tablename__ = "challans"
    id = Column(Integer, primary_key=True, index=True)
    dc_number = Column(String, nullable=True)
    dc_sequence = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    name = Column(String, nullable=True)
    project_name = Column(String, nullable=True)
    client = Column(String, nullable=True)
    location = Column(String, nullable=True)
    has_po = Column(String, default="no")
    po_number = Column(String, nullable=True)

class ChallanItem(Base):
    __tablename__ = "challan_items"
    id = Column(Integer, primary_key=True, index=True)
    challan_id = Column(Integer, ForeignKey("challans.id"), nullable=False)
    sno = Column(Integer, nullable=False)
    asset_id = Column(String, nullable=True)
    asset_name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    quantity = Column(Integer, default=1)
    serial_no = Column(String, nullable=True)
    returnable = Column(String, default="no")
    expected_return_date = Column(Date, nullable=True)
    returned_date = Column(Date, nullable=True)
    
    # Relationship
    challan = relationship("Challan", backref="items")