import unittest
from unittest.mock import patch
from main import what_is_year_now


class TestYear(unittest.TestCase):
    @patch("main.urllib.request.urlopen")
    @patch("main.json.load", return_value={"currentDateTime": "0000-00-00"})
    def test_yyyy_format(self, response, resp_json):
        result = what_is_year_now()

        self.assertEqual(result, 0)

    @patch("main.urllib.request.urlopen")
    @patch("main.json.load", return_value={"currentDateTime": "00.00.0000"})
    def test_dd_format(self, response, resp_json):
        result = what_is_year_now()

        self.assertEqual(result, 0)

    @patch("main.urllib.request.urlopen")
    @patch("main.json.load", return_value={"currentDateTime": "wrong_format"})
    def test_exception(self, response, resp_json):
        self.assertRaises(ValueError, what_is_year_now)
