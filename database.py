# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = os.environ.get(
#     "DATABASE_URL",
#     "postgresql://postgres:7410@localhost:5432/dc_generator_db"
# )

# engine = create_engine(
#     DATABASE_URL,
#     pool_pre_ping=True  # retries if connection fails
# )
# SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
# Base = declarative_base()

# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = os.environ.get(
#     "DATABASE_URL",
#     "postgresql://postgres:7410@localhost:5432/dc_generator_db"
# )

# engine = create_engine(
#     DATABASE_URL,
#     pool_pre_ping=True  # retries if connection fails
# )
# SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
# Base = declarative_base()

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://postgres:7410@localhost:5432/dc_generator_db"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True # retries if connection fails
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
