"""
test_date_detector.py - Unit test for date detection
This script contains tests for the date_detect function in the data_detector module.
It uses pytest for testing and parametrize to test multiple input-output scenarios.
Written by Sergey Torshin @torshin5ergey
"""

import pytest
from ..data_detector import date_detect

# Decorator for parametrizing a test function with multiple sets of input-expected
@pytest.mark.parametrize("text, expected", [
    ("Today is 2024-05-10 and tomorrow is 11/05/2024", "2024-05-10\n11/05/2024"),
    ("No dates in this text.", None),
    ("2022-01-01 is a date", "2022-01-01"),
    ("This is a date: 01-01-2022", "01-01-2022"),
    ("Another date: 2022/01/01", "2022/01/01"),
    ("Clean up dates in different date formats (such as 3/14/2019, 03-14-2019, and 2015/3/19) by replacing them with dates in a single, standard format.", "3/14/2019\n03-14-2019\n2015/3/19")
    ])

def test_data_detector(text, expected):
    assert date_detect(text) == expected
