import unittest
import json
from api.app.endpoints.auth import SignUp
from api.models.user import NormalUser, Admin
from api.tests import BaseTestCase

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
        self.assertEqual(signup.status_code,201)

    def test_user_login(self):
        """test a user can login"""
        signup = self.test_client.post(
            "/api/v1/auth/signup",
            data = json.dumps(dict(
                username = "Kulakula",
                email = "kula@gmail.com",
                password = "A123456789a!",
                confirm_password = "A123456789a!"
                )),
            headers = {"content-type":"application/json"}
            )

        login = self.test_client.post(
            "/api/v1/auth/login",
            data = json.dumps(dict(
                username = "Kulakula",
                password = "A123456789a!")),
            headers = {"content-type":"application/json"}
            )
        self.assertEqual(login.status_code,200)

    # def test_admin_can_approve_user(self):
    #     """test approve user by super admin"""
    #     save_admin = Admin.save(self)
    #     super_admin_login = self.test_client.post(
    #         "/api/v1/auth/login",
    #         data = json.dumps(dict(
    #             username = "admin",
    #             password = "A123456789a!"
    #             )),
    #         headers = {"content-type":"appliction/json"}
    #         )
    #     self.assertEqual(super_admin_login.status_code,200)


