'''
test_rabinkarp.py - Unit tests for rabin_karp() function

Written by Sergey Torshin @torshin5ergey
'''

import unittest
from rabinkarp import rabin_karp


class TestRabinKarp(unittest.TestCase):
    """Tests for rabin_karp()"""
    def setUp(self) -> None:
        return super().setUp()

    def test_smoke_rabin_karp(self):
        """Basic tests"""
        self.assertEqual(rabin_karp('Rabin Karp', 'Rabin'), 0)
        self.assertEqual(rabin_karp('Rabin Karp', 'Karp'), 6)
        self.assertEqual(rabin_karp('Rabin Karp', 'Rabin Karp'), 0)

    def test_edge_rabin_karp(self):
        """Edge tests"""
        self.assertEqual(rabin_karp('Rabin Karp', 'foo'), -1)
        self.assertEqual(rabin_karp('', 'foo'), -1)
        self.assertEqual(rabin_karp('Rabin Karp', ''), 0)
        self.assertEqual(rabin_karp('Rabin', 'Rabin Karp'), -1)

if __name__ == "__main__":
    unittest.main()