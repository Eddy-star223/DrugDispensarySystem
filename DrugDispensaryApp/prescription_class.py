class Prescription:
    def __init__(self, code, patient, diagnosis, drugs, doctor):
        self.code = code
        self.patient = patient
        self.diagnosis = diagnosis
        self.drugs = drugs
        self.doctor = doctor
        self.status = "Pending"

    def __str__(self):
        return f"Code: {self.code}, Patient: {self.patient}, Diagnosis: {self.diagnosis}, Drugs: {self.drugs}, Status: {self.status}"

