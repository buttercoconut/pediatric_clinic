from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL – replace with actual credentials
DATABASE_URL = "postgresql://user:password@localhost/pediatric_clinic"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency for FastAPI

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
