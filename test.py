import unittest
from main import get_user_info, print_database, input_userdata_into_db, print_user_in_db, get_username, parse_response


class TestMain(unittest.TestCase):
    def setUp(self):
        self.msg = """Breakfast:
                        - Berry Smoothie | mixed berries, banana, spinach
                        - Avocado Toast | whole grain bread, avocado,
                         cherry tomatoes
                        Lunch:
                        - Quinoa Salad | quinoa, mixed vegetables, chickpeas
                        - Grilled Chicken Salad | mixed greens,
                        grilled chicken, cucumbers
                        Dinner:
                        - Baked Salmon | salmon fillet, asparagus, quinoa
                        - Stir-Fried Tofu and Vegetables | tofu, bell peppers,
                        broccoli
                    """

    def test_print_database(self):
        print_database()

    def test_print_user_in_db(self):
        print_user_in_db()

    def test_get_username(self):
        self.assertEqual(get_username("RANDOM"), None)
        self.assertNotEqual(get_username("Rob"), None)

    def test_parse_response(self):
        parse_response(self.msg)
