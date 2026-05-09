from fastapi import FastAPI
from .routers import patients, doctors, appointments

app = FastAPI(title="Pediatric Clinic API")

app.include_router(patients.router)
app.include_router(doctors.router)
app.include_router(appointments.router)

# Create tables on startup
@app.on_event("startup")
def on_startup():
    from ..database.database import engine, Base
    Base.metadata.create_all(bind=engine)
