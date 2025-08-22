import unittest
from unittest.mock import patch

from DrugDispensaryApp.services.login_service import register_user

class TestAuthService(unittest.TestCase):
    @patch("builtins.input", side_effect=["Dr. wyser", "password123", "doctor"])
    def test_valid_login(self, mock_input):
        role = register_user()
        self.assertEqual(role, "doctor")



