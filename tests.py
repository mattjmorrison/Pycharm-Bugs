

import unittest


class TestForPy3660(unittest.TestCase):

    def test_that_the_pycharm_output_is_correct(self):
        """
        This produces the following in the console
        Failure
        Expected :'XXXXXXXXXX'
        Actual   :' != ''
        And should produce
        Failure
        Expected :'XXXXXXXXXX'
        Actual   :''
        """
        self.assertEqual('XXXXXXXXXX', '')