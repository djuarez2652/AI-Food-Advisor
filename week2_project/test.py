import unittest
from main import *

class TestMain(unittest.TestCase):

    def setUp(self):
        self.user = {
                    "name": "Rob",
                    "age": 18,
                    "currWeight": 140,
                    "goalWeight": 130,
                    "reason": "To lose weight"
                    }

    def test_get_user_info(self):        
        self.assertEqual(self.get_user_info(), self.user)

    def test_print_database(self):
        self.print_database()

    def test_input_userdata_into_db(self):
        self.input_userdata_into_db(self.user)

    def test_print_user_in_db(self):
        self.print_user_in_db()

    def test_get_username(self):
        self.assertEqual(self.get)