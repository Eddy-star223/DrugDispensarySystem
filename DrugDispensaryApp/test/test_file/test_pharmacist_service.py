import unittest

from DrugDispensaryApp.exceptions.custom_exception import PrescriptionNotFoundError, DispenseError
from DrugDispensaryApp.services.pharmacist_service import verify_prescription, dispense_drugs, view_fulfilled
from DrugDispensaryApp.services.doctor_services import create_prescription


class TestPharmacistService(unittest.TestCase):
    def setUp(self):
        self.code = create_prescription("doctor1", "John ", "Malaria", ["Coartem"])

    def test_verify_valid_code(self):
        p = verify_prescription(self.code)
        self.assertIsNotNone(p)
        self.assertEqual(p.code, self.code)

    def test_verify_invalid_code(self):
        def test_verify_invalid_code(self):
            with self.assertRaises(PrescriptionNotFoundError) as context:
                verify_prescription("INVALID")

            self.assertIn("Prescription with code INVALID not found", str(context.exception))

    def test_dispense_valid_code(self):
        success = dispense_drugs(self.code)
        self.assertTrue(success)

    def test_dispense_invalid_code(self):
        with self.assertRaises(DispenseError) as context:
            dispense_drugs("FAKECODE")

        self.assertIn("Invalid prescription code", str(context.exception))

    def test_view_fulfilled(self):
        dispense_drugs(self.code)
        fulfilled = view_fulfilled()
        self.assertTrue(any(p.code == self.code for p in fulfilled))