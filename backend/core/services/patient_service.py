from sqlalchemy.orm import Session
from ..database.database import get_db
from ..api.models.models import Patient, Doctor, Appointment, Record, Allergy

# Patient service

def get_patient(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.id == patient_id).first()

def create_patient(db: Session, patient_in):
    patient = Patient(**patient_in.dict())
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

# Doctor service

def get_doctor(db: Session, doctor_id: int):
    return db.query(Doctor).filter(Doctor.id == doctor_id).first()

def create_doctor(db: Session, doctor_in):
    doctor = Doctor(**doctor_in.dict())
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor

# Appointment service

def create_appointment(db: Session, appointment_in):
    appointment = Appointment(**appointment_in.dict())
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment

# Record service

def create_record(db: Session, record_in):
    record = Record(**record_in.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

# Allergy service

def create_allergy(db: Session, allergy_in, patient_id: int):
    allergy = Allergy(**allergy_in.dict(), patient_id=patient_id)
    db.add(allergy)
    db.commit()
    db.refresh(allergy)
    return allergy
