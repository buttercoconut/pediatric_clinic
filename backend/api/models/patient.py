"""Pydantic model for Patient."""

from pydantic import BaseModel, Field
from typing import List, Optional

class PatientBase(BaseModel):
    first_name: str = Field(..., example="John")
    last_name: str = Field(..., example="Doe")
    date_of_birth: str = Field(..., example="2015-06-15")
    gender: str = Field(..., example="Male")
    phone: Optional[str] = Field(None, example="010-1234-5678")
    email: Optional[str] = Field(None, example="john.doe@example.com")
    address: Optional[str] = Field(None, example="123 Main St, Seoul")

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int

    class Config:
        orm_mode = True
