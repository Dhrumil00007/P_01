from fastapi import APIRouter, HTTPException, status
from typing import List
from models.patient_model import PatientCreate, PatientUpdate, PatientResponse
from controllers import patient_controller

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.post(
    "/postpatients",
    response_model=PatientResponse,
    status_code=status.HTTP_201_CREATED
)
def create_patient(patient: PatientCreate):
    return patient_controller.create_patient(patient)


@router.get(
    "/getpatients",
    response_model=List[PatientResponse],
    status_code=status.HTTP_200_OK
)
def get_all_patients():
    return patient_controller.get_all_patients()


@router.get(
    "/getpatient/{patientid}",
    response_model=PatientResponse,
    status_code=status.HTTP_200_OK
)
def get_patient_by_id(patientid: int):
    patient = patient_controller.get_patient_by_id(patientid)

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patientid} not found"
        )

    return patient


@router.delete(
    "/deletepatient/{patientid}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_patient(patientid: int):
    success = patient_controller.delete_patient(patientid)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patientid} not found"
        )

    return None


@router.put(
    "/updatepatient/{patientid}",
    response_model=PatientResponse,
    status_code=status.HTTP_200_OK
)
def update_patient(patientid: int, patient: PatientUpdate):
    updated = patient_controller.update_patient(patientid, patient)

    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patientid} not found"
        )

    return updated