from sqlalchemy import Column, Integer, String, Date, Text, Boolean
from database import Base


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
    client = Column(String, nullable=False)
    location = Column(String, nullable=False)
    has_po = Column(String(10))
    po_number = Column(String)
    project_name = Column(String, nullable=False)
    project_details = Column(Text)
    field_supervisor = Column(String)
    persons_involved = Column(Text)  

class Challan(Base):
    __tablename__ = "challans"
    id = Column(Integer, primary_key=True, index=True)
    dc_number = Column(String, unique=True, nullable=False)
    dc_sequence = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    name = Column(String)
    project_name = Column(String)
    client = Column(String)
    location = Column(String)
    has_po = Column(String)
    po_number = Column(String)

class ChallanItem(Base):
    __tablename__ = "challan_items"
    id = Column(Integer, primary_key=True, index=True)
    challan_id = Column(Integer, nullable=False)
    sno = Column(Integer)
    asset_name = Column(String)
    description = Column(String)
    quantity = Column(Integer)
    serial_no = Column(String)
    returnable = Column(String)
    expected_return_date = Column(Date)
    returned_date = Column(Date)

from sqlalchemy import Column, Integer, String, Date, Text, Boolean, ForeignKey
from database import Base

class Asset(Base):
    __tablename__ = "assets"
    
    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(String, unique=True, nullable=False)
    asset_name = Column(String, nullable=False)
    category = Column(String)
    make_model = Column(String)
    serial_number = Column(String, unique=True)
    supplier_details = Column(Text)
    date_of_purchase = Column(Date)
    warranty_details = Column(Text)
    last_service_date = Column(Date)
    covered_under_amc = Column(Boolean, default=False)
    amc_vendor_details = Column(Text)
    condition = Column(String)
    status = Column(String, default="active")
    
    # Transaction details
    transaction_date = Column(Date)
    transaction_type = Column(String)  # inward/outward
    received_from = Column(String)
    purpose = Column(String)
    issued_by = Column(String)
    received_by = Column(String)
    expected_return_date = Column(Date)
    returned_date = Column(Date)
    is_received = Column(Boolean, default=False)
    
    # Disposal details
    disposal_approvals_obtained = Column(Boolean, default=False)
    date_of_approval = Column(Date)
    approved_by = Column(String)
    media_sanitised = Column(Boolean, default=False)
    media_sanitised_by = Column(String)
    date_of_media_sanitisation = Column(Date)