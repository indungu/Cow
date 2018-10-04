import unittest
import json
from flask import request, jsonify
from datetime import datetime
from app.endpoints.cow_construction import ConstructionProcess
from models.cow_model import CowAssemblyModel
from tests import BaseTestCase

assembly_time =datetime.now()

class Test_Cow_Construction(BaseTestCase):
    """test cow construction"""

    def test_update_cow(self):
        """test a user can update a cow"""
        milk_entry =self.test_client.post(
            "/api/v1/cow/milk",
            data = json.dumps(dict(
                moo_name = "Bronze",
                breed = "Bull",
                age = "2",
                cow_health="Needs a mate",
                time = str(assembly_time)
                )),
            headers = {"content-type":"application/json"}
            )
        # self.assertEqual(milk_entry.status_code,201)

        # get the cow
        update_cow = self.test_client.put("/api/v1/cow/1",
                data = json.dumps(dict(
                    moo_name = "Bronze",
                    breed = "Bull",
                    age = "3",
                    cow_health="Had menengitis last year"
                    )),
                headers = {"content-type":"application/json"}
            )
        self.assertEqual(update_cow.status_code,200 )
