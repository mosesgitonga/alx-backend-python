#!/usr/bin/env python3
"""
parameterize a unit test
"""
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    path output
    """
    @parameterized.expand([
        ({"a": 1}, {"a",}, 1), 
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected)

    @parameterized.expand([
        ({"a": 1}, ("a", "b"), "KeyError")
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        try:
            res = access_nested_map(nested_map, path)
            self.assertEqual(res, expected)
        except KeyError as e:
            return "KeyError"
