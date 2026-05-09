"""SQLAlchemy model for Appointment."""

from sqlalchemy import Column, Integer, String, ForeignKey
from ..database.database import Base

class AppointmentDB(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    appointment_time = Column(String, nullable=False)
    reason = Column(String, nullable=True)
