"""Pydantic model for Appointment."""

from pydantic import BaseModel, Field
from typing import Optional

class AppointmentBase(BaseModel):
    patient_id: int = Field(..., example=1)
    doctor_id: int = Field(..., example=2)
    appointment_time: str = Field(..., example="2024-10-01T10:00:00Z")
    reason: Optional[str] = Field(None, example="Routine check-up")

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int

    class Config:
        orm_mode = True
