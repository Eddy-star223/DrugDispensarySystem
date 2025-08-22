import unittest
from DrugDispensaryApp.services.login_service import register_user

class TestAuthService(unittest.TestCase):
    def test_valid_login(self):
        role = register_user()
        self.assertEqual(role, "doctor")

    def test_invalid_login(self):
        role = register_user()
        self.assertIsNone(role)

    def test_empty_credentials(self):
        role = register_user()
        self.assertIsNone(role)