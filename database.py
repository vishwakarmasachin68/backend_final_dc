from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:7410@localhost:5432/dc_generator_db" 
# DATABASE_URL="postgresql://postgres:7410@localhost:5432/delivery_challan_final_backend"
 # Change as required

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

