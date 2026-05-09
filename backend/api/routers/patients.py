from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..api.models.models import Patient
from ..core.services.patient_service import create_patient, get_patient

router = APIRouter(prefix="/patients", tags=["patients"])

@router.post("/", response_model=Patient.PatientRead, status_code=status.HTTP_201_CREATED)
def create_patient_endpoint(patient_in: Patient.PatientCreate, db: Session = Depends(get_db)):
    patient = create_patient(db, patient_in)
    return patient

@router.get("/{patient_id}", response_model=Patient.PatientRead)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient
