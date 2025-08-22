from DrugDispensaryApp.repositories.store_prescription import get_by_code, get_fulfilled_by_pharmacist
from DrugDispensaryApp.exceptions.custom_exception import PrescriptionNotFoundError, DispenseError

def verify_prescription(code):
    prescription = get_by_code(code)
    if not prescription:
        raise PrescriptionNotFoundError(f"Prescription with code {code} not found")
    return prescription

def dispense_drugs(code):
    prescription = get_by_code(code)
    if not prescription:
        raise DispenseError("Invalid prescription code")
    if prescription.status == "Dispensed":
        raise DispenseError("Prescription already dispensed")
    prescription.status = "Dispensed"
    return True

def view_fulfilled():
    return get_fulfilled_by_pharmacist()