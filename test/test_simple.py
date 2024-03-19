# coding: utf-8

"""
    httpbin.org

    A simple HTTP Request & Response Service.<br/> <br/> <b>Run locally: </b> <code>$ docker run -p 80:80 kennethreitz/httpbin</code>

    The version of the OpenAPI document: 0.9.2
    Contact: me@kennethreitz.org
    Created by: https://kennethreitz.org
"""

import unittest

import os
from pprint import pprint
from httpbin_python_sdk import Httpbin

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        httpbin = Httpbin(
        )
        self.assertIsNotNone(httpbin)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
