# coding: utf-8

"""
    httpbin.org

    A simple HTTP Request & Response Service.<br/> <br/> <b>Run locally: </b> <code>$ docker run -p 80:80 kennethreitz/httpbin</code>

    The version of the OpenAPI document: 0.9.2
    Contact: me@kennethreitz.org
    Created by: https://kennethreitz.org
"""

import unittest

import httpbin_python_sdk
from httpbin_python_sdk.model.redirects_to_given_url_post_request import RedirectsToGivenUrlPostRequest
from httpbin_python_sdk import configuration


class TestRedirectsToGivenUrlPostRequest(unittest.TestCase):
    """RedirectsToGivenUrlPostRequest unit test stubs"""
    pass


if __name__ == '__main__':
    unittest.main()
