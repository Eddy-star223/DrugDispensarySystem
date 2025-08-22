
from DrugDispensaryApp.data.model.user_prescription import Prescription

prescriptions = []

def save_prescription(prescription):
    prescriptions.append(prescription)

def get_by_code(code):
    return next((p for p in prescriptions if p.code == code), None)

def get_by_doctor(doctor):
    return [p for p in prescriptions if p.doctor == doctor]

def get_fulfilled_by_pharmacist():
    return [p for p in prescriptions if p.status == "Dispensed"]