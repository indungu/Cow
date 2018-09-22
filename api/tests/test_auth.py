import unittest
import json
from app.endpoints.auth import SignUp
from tests import BaseTestCase

class Test_SignUp(BaseTestCase):
    """Test user signup"""

    def test_signup(self):
        """Test a normal user can signup"""
        signup = self.test_client.post(
            "/api/v1/auth/signup",
            data = json.dumps(dict(
                username = "Naibor",
                email = "hello@gmail.com",
                password = "A123456789a!",
                confirm_password = "A123456789a!"
                )),
            headers = {"content-type":"application/json"}
            )
        # import pdb; pdb.set_trace()
        self.assertEqual(signup.status_code,200)

    def test_user_login(self):
        """test a user can login"""
        login = self.test_client.post(
            "/api/v1/auth/login",
            data = json.dumps(dict(
                username = "Naibor",
                password = "A123456789a!")),
            headers = {"content-type":"application/json"}
            )
        self.assertEqual(login.status_code,200)
