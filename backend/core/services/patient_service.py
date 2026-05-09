"""Patient service layer."""

from sqlalchemy.orm import Session
from ..models.patient_db import PatientDB
from ..models.patient import PatientCreate

class PatientService:
    def __init__(self, db: Session):
        self.db = db

    def create_patient(self, patient_in: PatientCreate) -> PatientDB:
        patient = PatientDB(**patient_in.dict())
        self.db.add(patient)
        self.db.commit()
        self.db.refresh(patient)
        return patient

    def get_patient(self, patient_id: int) -> PatientDB:
        return self.db.query(PatientDB).filter(PatientDB.id == patient_id).first()
