# coding: utf-8

# flake8: noqa

"""
    httpbin.org

    A simple HTTP Request & Response Service.<br/> <br/> <b>Run locally: </b> <code>$ docker run -p 80:80 kennethreitz/httpbin</code>

    The version of the OpenAPI document: 0.9.2
    Contact: me@kennethreitz.org
    Created by: https://kennethreitz.org
"""

__version__ = "0.9.2"

# import ApiClient
from httpbin_python_sdk.api_client import ApiClient

# import Configuration
from httpbin_python_sdk.configuration import Configuration

# import exceptions
from httpbin_python_sdk.exceptions import OpenApiException
from httpbin_python_sdk.exceptions import ApiAttributeError
from httpbin_python_sdk.exceptions import ApiTypeError
from httpbin_python_sdk.exceptions import ApiValueError
from httpbin_python_sdk.exceptions import ApiKeyError
from httpbin_python_sdk.exceptions import ApiException

from httpbin_python_sdk.client import Httpbin
