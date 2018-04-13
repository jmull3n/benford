# -*- coding: utf-8 -*-

import unittest
from lab7_benford_calculator.core import benford


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    def setUp(self):        
            config={"file_name": "./tests/census_2009_test.tsv", "numeric_column":"blah"}
            self.expected_result = {1: 4, 2: 6, 3: 2, 4: 2, 5: 0, 6: 0, 7: 3, 8: 2, 9: 1}
            self.benfordCalculator = benford.BenfordCalculator(configuration=config)

    def test_benford(self):
        self.benfordCalculator.process_file()
        print("output: {}".format(self.benfordCalculator.get_raw_output()))
        assert self.benfordCalculator.get_raw_output()==self.expected_result


if __name__ == '__main__':
    unittest.main()