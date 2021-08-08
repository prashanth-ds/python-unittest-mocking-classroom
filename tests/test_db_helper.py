from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper


class TestCalculator(TestCase):
    def setUp(self):
        self.db_obj = DbHelper()

    @patch('src.db_helper.DbHelper')
    def test_max_salary_is_greater_than_min_salary(self, MockDatabase):
        databaseObject = MockDatabase()  # create a mock object of DBHelper class. This will help to customize output of class methods

        databaseObject.get_maximum_salary.return_value = 67000
        max = databaseObject.get_maximum_salary()
        expected_max = 67000

        databaseObject.get_minimum_salary.return_value = 27000
        min = databaseObject.get_minimum_salary()
        expected_min = 27000

        self.assertEqual(max, expected_max)
        self.assertEqual(min, expected_min)
        self.assertGreater(max, min)


