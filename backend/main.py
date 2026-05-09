"""Main entry point for the FastAPI application."""

from fastapi import FastAPI
from .api.routers import appointments, patients
from .database.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pediatric Clinic API")

# Include routers
app.include_router(patients.router, prefix="/patients", tags=["patients"])
app.include_router(appointments.router, prefix="/appointments", tags=["appointments"])

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Pediatric Clinic API"}
