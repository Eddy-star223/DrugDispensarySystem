import unittest
from DrugDispensaryApp.data.model.user_prescription import Prescription


class TestPrescriptionModel(unittest.TestCase):
    def test_prescription_initialization(self):
        p = Prescription("RX001", "Dr. Wyser", "John Doe", "Malaria", ["Paracetamol", "Coartem"])
        self.assertEqual(p.code, "RX001")
        self.assertEqual(p.status, "Pending")

    def test_prescription_str_output(self):
        p = Prescription("RX002", "Dr. Wyser", "Jane Doe", "Typhoid", ["Flagyl"])
        output = str(p)
        self.assertIn("Code: RX002", output)
        self.assertIn("Drugs: Flagyl", output)