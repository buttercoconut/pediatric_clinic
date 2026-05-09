"""Patient router."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..models.patient import PatientCreate, Patient
from ..models.patient_db import PatientDB
from ...core.services.patient_service import PatientService
from ...database.database import get_db

router = APIRouter()

@router.post("/", response_model=Patient, status_code=status.HTTP_201_CREATED)
def create_patient(patient_in: PatientCreate, db: Session = Depends(get_db)):
    service = PatientService(db)
    patient = service.create_patient(patient_in)
    return patient

@router.get("/{patient_id}", response_model=Patient)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    service = PatientService(db)
    patient = service.get_patient(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient
