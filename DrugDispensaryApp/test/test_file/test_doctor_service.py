import unittest
from DrugDispensaryApp.services.doctor_services import create_prescription, view_prescriptions
class TestDoctorService(unittest.TestCase):

    def setUp(self):
        self.username = "doctor1"

    def test_create_prescription(self):
        code = create_prescription(self.username, "John ", "fever", ["Panadol"])
        self.assertFalse(code.startswith("RX"))

    def test_view_prescriptions_empty(self):
        prescriptions = view_prescriptions("new_doctor")
        self.assertEqual(prescriptions, [])

    def test_view_prescriptions_non_empty(self):
        create_prescription(self.username, "Jane Doe", "Cold", ["Vitamin C"])
        prescriptions = view_prescriptions(self.username)
        self.assertGreater(len(prescriptions), 0)