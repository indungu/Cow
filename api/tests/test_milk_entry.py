import unittest
import json
from datetime import datetime
from app.endpoints.milking import MilkingProcess
from models.milk_model import MilkingProcessModel
# from models.milk_model import average_milk
from tests import BaseTestCase

milking_time =datetime.now()

class Test_Milk_Entry(BaseTestCase):
    """test milk entries"""

    def test_save_milk(self):
        """test a user can save milk entry"""
        milk_entry =self.test_client.post(
            "/api/v1/cow/milk",
            data = json.dumps(dict(
                amount = "13.66",
                time = str(milking_time)
                # average = MilkingProcessModel.average_milk()
                )),
            headers = {"content-type":"application/json"}
            )
        self.assertEqual(milk_entry.status_code,201)


