"""Appointment service layer."""

from sqlalchemy.orm import Session
from ..models.appointment_db import AppointmentDB
from ..models.appointment import AppointmentCreate

class AppointmentService:
    def __init__(self, db: Session):
        self.db = db

    def create_appointment(self, appointment_in: AppointmentCreate) -> AppointmentDB:
        appointment = AppointmentDB(**appointment_in.dict())
        self.db.add(appointment)
        self.db.commit()
        self.db.refresh(appointment)
        return appointment

    def get_appointment(self, appointment_id: int) -> AppointmentDB:
        return self.db.query(AppointmentDB).filter(AppointmentDB.id == appointment_id).first()
