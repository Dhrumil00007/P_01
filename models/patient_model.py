from pydantic import BaseModel, Field


class PatientBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, example='Rahul Patel')
    age: int = Field(..., ge=0, example=25)
    disease: str = Field(..., min_length=2, max_length=100, example='Fever')

class PatientCreate(PatientBase):
    pass

class PatientUpdate(PatientBase):
    pass
class PatientResponse(PatientBase):
    id: int

    class Config:
        from_attributes = True
