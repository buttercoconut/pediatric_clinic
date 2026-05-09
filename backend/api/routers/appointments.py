from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..api.models.models import Appointment
from ..core.services.patient_service import create_appointment

router = APIRouter(prefix="/appointments", tags=["appointments"])

@router.post("/", response_model=Appointment.AppointmentRead, status_code=status.HTTP_201_CREATED)
def create_appointment_endpoint(appointment_in: Appointment.AppointmentCreate, db: Session = Depends(get_db)):
    appointment = create_appointment(db, appointment_in)
    return appointment

# Additional endpoints (list, get) can be added similarly
