from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..api.models.models import Doctor
from ..core.services.patient_service import create_doctor, get_doctor

router = APIRouter(prefix="/doctors", tags=["doctors"])

@router.post("/", response_model=Doctor.DoctorRead, status_code=status.HTTP_201_CREATED)
def create_doctor_endpoint(doctor_in: Doctor.DoctorCreate, db: Session = Depends(get_db)):
    doctor = create_doctor(db, doctor_in)
    return doctor

@router.get("/{doctor_id}", response_model=Doctor.DoctorRead)
def read_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = get_doctor(db, doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor
