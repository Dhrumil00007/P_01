from typing import List, Optional
from models.patient_model import PatientCreate, PatientUpdate, PatientResponse

patients_db: List[dict] = []
current_id: int = 1


def get_all_patients() -> List[dict]:
    return patients_db

def get_patient_by_id(patient_id: int) -> Optional[dict]:
    for patient in patients_db:
        if patient["id"] == patient_id:
            return patient
    return None


def create_patient(patient_data: PatientCreate) -> dict:
    global current_id
    new_patient = {
        "id": current_id,
        "name": patient_data.name,
        "age": patient_data.age,
        "disease": patient_data.disease,
    }
    patients_db.append(new_patient)
    current_id += 1
    return new_patient


def update_patient(patient_id: int, patient_data: PatientUpdate) -> Optional[dict]:
    for patient in patients_db:
        if patient["id"] == patient_id:
            patient["name"] = patient_data.name
            patient["age"] = patient_data.age
            patient["disease"] = patient_data.disease
            return patient
    return None


def delete_patient(patient_id: int) -> bool:
    for index, patient in enumerate(patients_db):
        if patient["id"] == patient_id:
            patients_db.pop(index)
            return True
    return False
