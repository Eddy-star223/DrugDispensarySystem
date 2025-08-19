class PrescriptionResponse:
    def __init__(self, code, patient_name, diagnosis, drugs, status):
        self.code = code
        self.patient_name = patient_name
        self.diagnosis = diagnosis
        self.drugs = drugs
        self.status = status
