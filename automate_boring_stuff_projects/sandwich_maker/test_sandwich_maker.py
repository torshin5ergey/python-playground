'''
test_sandwich_maker.py - 

Written by Sergey Torshin @torshin5ergey
'''

import random

import unittest
from unittest.mock import patch

from sandwich_maker import Sandwich



class TestSandwich(unittest.TestCase):


    def setUp(self) -> None:
        """Initialize a new Sandwich object before test."""
        self.sandwich = Sandwich()


    @patch('pyinputplus.inputMenu')
    def test_choose_bread(self, mock_input):
        """Choose bread test"""
        # Mocking user input with random bread type
        random_bread = random.choice(list(self.sandwich.bread_prices.keys()))
        mock_input.return_value = random_bread

        self.sandwich.choose_bread()
        self.assertEqual(self.sandwich.bread, random_bread)


    @patch('pyinputplus.inputMenu')
    def test_choose_protein(self, mock_input):
        """Choose protein test"""
        # Mocking user input with random protein type
        random_protein = random.choice(list(self.sandwich.protein_prices.keys()))
        mock_input.return_value = random_protein

        self.sandwich.choose_protein()
        self.assertEqual(self.sandwich.protein, random_protein)


    @patch('pyinputplus.inputYesNo')
    @patch('pyinputplus.inputMenu')
    def test_choose_cheese(self, mock_input, mock_yesno):
        """Choose cheese test"""
        # Mocking user input to confirm cheese
        mock_yesno.return_value = 'yes'

        # Mocking user input with random cheese type
        random_cheese = random.choice(list(self.sandwich.cheese_prices.keys()))
        mock_input.return_value = random_cheese

        self.sandwich.choose_cheese()
        self.assertEqual(self.sandwich.cheese, random_cheese)


    @patch('pyinputplus.inputYesNo')
    @patch('pyinputplus.inputMenu')
    def test_choose_extra(self, mock_input, mock_yesno):
        """Choose extra test"""
        # Mocking user input to confirm extra, confirm more extra and no
        # Every call it will returns 'yes', 'yes', 'no' sequentially
        mock_yesno.side_effect = ['yes', 'yes', 'no']  

        # Mocking user input with random extra
        available_extra_list = list(self.sandwich.extra_prices.keys())
        random_extra = []
        for _ in range(2):
            choosen_extra = random.choice(available_extra_list)
            random_extra.append(choosen_extra)
            available_extra_list.remove(choosen_extra)
        mock_input.side_effect = random_extra

        self.sandwich.choose_extra()
        self.assertEqual(self.sandwich.extra, random_extra)

    
    def test_calculate_total(self):
        """Calculate total coast test"""
        self.sandwich.bread = 'wheat'
        self.sandwich.protein = 'turkey'
        self.sandwich.cheese = 'Swiss'
        self.sandwich.extra = ['tomato', 'lettuce']
        self.sandwich.calculate_total()
        expected_total = 6.5
        self.assertEqual(self.sandwich.total_cost, expected_total)
    

if __name__ == "__main__":
    unittest.main()