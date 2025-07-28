from sqlalchemy import Column, Integer, String, Date, Text
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
    persons_involved = Column(Text)  # store as JSON string

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
