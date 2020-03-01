import unittest
from src import response_creator


class TestResponseCreator(unittest.TestCase):

    def test_should_return_good_status_when_all_services_are_good(self):
        train_statuses = [
            {'name': 'Bakerloo', 'description': 'Good Service', 'reason': ''},
            {'name': 'Central', 'description': 'Good Service', 'reason': ''},
            {'name': 'Circle', 'description': 'Good Service', 'reason': ''}
        ]

        response = response_creator.create_response(train_statuses)
        self.assertEqual(response, "Good service on all lines")

    def test_should_return_bad_status_for_two_lines(self):
        train_statuses = [
            {'name': 'Bakerloo', 'description': 'Part Closure', 'reason': ''},
            {'name': 'Central', 'description': 'Good Service', 'reason': ''},
            {'name': 'Circle', 'description': 'Good Service', 'reason': ''},
            {'name': 'Piccadilly', 'description': 'Part Closure',
             'reason': 'PICCADILLY LINE: Saturday 29 February and Sunday 1 March'}
        ]

        response = response_creator.create_response(train_statuses)
        self.assertTrue("Bad service on 2 lines. " in response)

    def test_should_indicate_favorite_lines_disrupted(self):
        train_statuses = [
            {'name': 'Bakerloo', 'description': 'Part Closure', 'reason': ''},
            {'name': 'Central', 'description': 'Good Service', 'reason': ''},
            {'name': 'Circle', 'description': 'Good Service', 'reason': ''},
            {'name': 'Piccadilly', 'description': 'Part Closure', 'reason': ''}
        ]

        response = response_creator.create_response(train_statuses)
        self.assertEqual("Bad service on 2 lines. Your journey may be affected on the following lines, Piccadilly", response)


if __name__ == '__main__':
    unittest.main()
