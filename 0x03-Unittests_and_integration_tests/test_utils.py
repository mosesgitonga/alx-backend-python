#!/usr/bin/env python3
"""
parameterize a unit test
"""
import unittest
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([({"a": {"b": {"c": 1}}}, {"a": {"b": {"c": 1}}}), (1, 1)])
    def test_access_map(self, input, expected):
        self.assertEqual(input, expected)

if __name__ == "__main__":
    unittest.main()
