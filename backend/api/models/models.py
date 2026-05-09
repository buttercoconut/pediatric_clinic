from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..database.database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)

    allergies = relationship("Allergy", back_populates="patient", cascade="all, delete-orphan")
    appointments = relationship("Appointment", back_populates="patient", cascade="all, delete-orphan")
    records = relationship("Record", back_populates="patient", cascade="all, delete-orphan")

    # Pydantic schemas
    class PatientCreate:
        first_name: str
        last_name: str
        date_of_birth: str  # ISO format
        phone: str | None = None
        email: str | None = None

    class PatientRead:
        id: int
        first_name: str
        last_name: str
        date_of_birth: str
        phone: str | None
        email: str | None


class Allergy(Base):
    __tablename__ = "allergies"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    name = Column(String, nullable=False)

    patient = relationship("Patient", back_populates="allergies")

    class AllergyCreate:
        name: str

    class AllergyRead:
        id: int
        name: str


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    specialty = Column(String, nullable=True)

    appointments = relationship("Appointment", back_populates="doctor", cascade="all, delete-orphan")

    class DoctorCreate:
        first_name: str
        last_name: str
        specialty: str | None = None

    class DoctorRead:
        id: int
        first_name: str
        last_name: str
        specialty: str | None


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    appointment_time = Column(DateTime, nullable=False)
    reason = Column(String, nullable=True)

    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")

    class AppointmentCreate:
        patient_id: int
        doctor_id: int
        appointment_time: str  # ISO datetime
        reason: str | None = None

    class AppointmentRead:
        id: int
        patient_id: int
        doctor_id: int
        appointment_time: str
        reason: str | None


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    visit_date = Column(DateTime, nullable=False)
    notes = Column(String, nullable=True)

    patient = relationship("Patient", back_populates="records")
    doctor = relationship("Doctor")

    class RecordCreate:
        visit_date: str
        notes: str | None = None

    class RecordRead:
        id: int
        visit_date: str
        notes: str | None
