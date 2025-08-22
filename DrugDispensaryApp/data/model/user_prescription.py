
from dataclasses import dataclass

@dataclass
class Prescription:
    code: str
    doctor: str
    patient_name: str
    diagnosis: str
    drugs: list
    status: str = "Pending"

    def __str__(self):
        return (
            f"Code: {self.code}\n"
            f"Doctor: {self.doctor}\n"
            f"Patient: {self.patient_name}\n"
            f"Diagnosis: {self.diagnosis}\n"
            f"Drugs: {', '.join(map(str, self.drugs))}\n"
            f"Status: {self.status}\n"
        )
