#!/usr/bin/env python3
"""
parameterize a unit test
"""
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    path output
    """
    @parameterized.expand([
        ({"a": 1}, {"a", }, 1),
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
        """
        give exception
        """
        try:
            res = access_nested_map(nested_map, path)
            self.assertEqual(res, expected)
        except KeyError as e:
            return "KeyError"


class TestGetJson(unittest.TestCase):
    """
    making fake requests
    """
    @patch("utils.requests.get")
    def test_get_json(self, mock_requests_get):
        """
        testing get json reqquests
        """

        test_data = [
            {"test_url": "http://example.com", "test_payload": {
                "payload": True}},
            {"test_url": "http://holberton.io", "test_payload": {
                "payload": False}}
        ]

        for data in test_data:
            mock_response = Mock()
            mock_response.json.return_value = data["test_payload"]

            mock_requests_get.return_value = mock_response

            result = get_json(data['test_url'])
            mock_requests_get.assert_called_once_with(data['test_url'])

            self.assertEqual(result, data['test_payload'])
            mock_requests_get.reset_mock()


class TestMemoize(unittest.TestCase):
    """
    test utils.memoize
    """
    def test_memoize(self):
        class TestClass:
            @patch('utils.memoize')
            def a_method(self, ):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        class TestClass:
            """tests class for testing with moize
            """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

            with patch.object(TestClass, 'a_method') as mock:
                test_class = TestClass()
                test_class.a_property()
                test_class.a_property()
                mock.assert_called_once()
