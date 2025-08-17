from DrugDispensaryApp.drug_dispensary_management_class import DrugDispensarySystem
import unittest

class TestDrugDispensarySystem(unittest.TestCase):
    def setUp(self):
        self.system = DrugDispensarySystem()
        self.system.register_user("doc1", "pass123", "doctor")
        self.system.register_user("pharm1", "meds456", "pharmacist")

    def test_login_success(self):
        user = self.system.login_user("doc1", "pass123")
        self.assertIsNotNone(user)
        self.assertEqual(user.role, "doctor")

    def test_login_fail(self):
        user = self.system.login_user("doc1", "wrongpass")
        self.assertIsNone(user)

    def test_duplicate_user(self):
        self.system.register_user("doc1", "newpass", "doctor")
        self.assertEqual(len(self.system.users), 2)  # Should not add duplicate

    def test_prescription_creation(self):
        doctor = self.system.users["doc1"]
        p = doctor.create_prescription("John Doe", "Malaria", ["Paracetamol"])
        self.assertEqual(p.patient, "John Doe")
        self.assertEqual(p.status, "Pending")

    def test_invalid_prescription_code(self):
        pharmacist = self.system.users["pharm1"]
        result = pharmacist.verify_prescription("fakecode", [])
        self.assertIsNone(result)

    def test_dispense_twice(self):
        doctor = self.system.users["doc1"]
        pharmacist = self.system.users["pharm1"]
        p = doctor.create_prescription("Jane", "Typhoid", ["Amoxicillin"])
        pharmacist.dispense_drugs(p)
        self.assertEqual(p.status, "Dispensed")
        pharmacist.dispense_drugs(p)  # Try again
        self.assertEqual(len(pharmacist.fulfilled), 2)