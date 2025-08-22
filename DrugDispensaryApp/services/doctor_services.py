
from DrugDispensaryApp.data.model.user_prescription import Prescription
from DrugDispensaryApp.repositories.store_prescription import save_prescription, get_by_doctor
from DrugDispensaryApp.utils.code_generator import generate_code


def create_prescription(doctor, patient_name, diagnosis, drugs):
    code = generate_code()
    prescription = Prescription(code, doctor, patient_name, diagnosis, drugs)
    save_prescription(prescription)
    return code

def view_prescriptions(doctor):
    return get_by_doctor(doctor)