import unittest
from main import *

class TestMain(unittest.TestCase):

    def setUp(self):
        self.user = {
                    "name": "Test",
                    "age": 18,
                    "currWeight": 140,
                    "goalWeight": 130,
                    "reason": "To lose weight"
                    }
        self.msg = """Breakfast:
                        - Berry Smoothie | mixed berries, banana, spinach
                        - Avocado Toast | whole grain bread, avocado, cherry tomatoes
                        Lunch:
                        - Quinoa Salad | quinoa, mixed vegetables, chickpeas
                        - Grilled Chicken Salad | mixed greens, grilled chicken, cucumbers
                        Dinner:
                        - Baked Salmon | salmon fillet, asparagus, quinoa
                        - Stir-Fried Tofu and Vegetables | tofu, bell peppers, broccoli
                    """

    def test_get_user_info(self):        
        self.assertEqual(self.get_user_info(), self.user)

    def test_print_database(self):
        self.print_database()

    def test_input_userdata_into_db(self):
        self.input_userdata_into_db(self.user)

    def test_print_user_in_db(self):
        self.print_user_in_db()

    def test_get_username(self):
        self.assertEqual(self.get_username("RANDOM"), None)
        self.assertNotEqual(self.get_username("Rob"), None)

    def test_parse_response(self):
        self.test_parse_response(self.msg)