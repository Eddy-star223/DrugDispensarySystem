import bcrypt
import uuid

from DrugDispensaryApp.prescription_class import Prescription

USERS = "users.txt"

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password_hash = self.hash_password(password)
        self.role = role

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def register(self, password):
        hpass = password.hash_password(password)
        with open(USERS, "a") as file:
            file.write(f'{password},{hpass}\n')
        return "registration successful"

class Doctor(User):
    def __init__(self, username, password):
        super().__init__(username, password, role="doctor")
        self.prescriptions = []

    def create_prescription(self, patient, diagnosis, drugs):
        code = str(uuid.uuid4())[:8]
        prescription = Prescription(code, patient, diagnosis, drugs, self.username)
        self.prescriptions.append(prescription)
        return prescription

    def view_prescription_history(self):
        return self.prescriptions

class Pharmacist(User):
    def __init__(self, username, password):
        super().__init__(username, password, role="pharmacist")
        self.fulfilled = []

    def verify_prescription(self, code, all_prescriptions):
        for p in all_prescriptions:
            if p.code == code:
                return p
        return None

    def dispense_drugs(self, prescription):
        prescription.status = "Dispensed"
        self.fulfilled.append(prescription)

    def view_fulfilled_history(self):
        return self.fulfilled
