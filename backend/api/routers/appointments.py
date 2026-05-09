"""Appointment router."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..models.appointment import AppointmentCreate, Appointment
from ..models.appointment_db import AppointmentDB
from ...core.services.appointment_service import AppointmentService
from ...database.database import get_db

router = APIRouter()

@router.post("/", response_model=Appointment, status_code=status.HTTP_201_CREATED)
def create_appointment(appointment_in: AppointmentCreate, db: Session = Depends(get_db)):
    service = AppointmentService(db)
    appointment = service.create_appointment(appointment_in)
    return appointment

@router.get("/{appointment_id}", response_model=Appointment)
def read_appointment(appointment_id: int, db: Session = Depends(get_db)):
    service = AppointmentService(db)
    appointment = service.get_appointment(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment
