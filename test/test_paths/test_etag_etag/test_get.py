# coding: utf-8

"""
    httpbin.org

    A simple HTTP Request & Response Service.<br/> <br/> <b>Run locally: </b> <code>$ docker run -p 80:80 kennethreitz/httpbin</code>

    The version of the OpenAPI document: 0.9.2
    Contact: me@kennethreitz.org
    Created by: https://kennethreitz.org
"""

import unittest
from unittest.mock import patch

import urllib3

import httpbin_python_sdk
from httpbin_python_sdk.paths.etag_etag import get
from httpbin_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestEtagEtag(ApiTestMixin, unittest.TestCase):
    """
    EtagEtag unit test stubs
        Assumes the resource has the given etag and responds to If-None-Match and If-Match headers appropriately.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
