# coding: utf-8

"""
    httpbin.org

    A simple HTTP Request & Response Service.<br/> <br/> <b>Run locally: </b> <code>$ docker run -p 80:80 kennethreitz/httpbin</code>

    The version of the OpenAPI document: 0.9.2
    Contact: me@kennethreitz.org
    Created by: https://kennethreitz.org
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from httpbin_python_sdk.type.model_int import ModelInt

class RequiredRedirectsToGivenUrlPostRequest(TypedDict):
    url: str

class OptionalRedirectsToGivenUrlPostRequest(TypedDict, total=False):
    status_code: ModelInt

class RedirectsToGivenUrlPostRequest(RequiredRedirectsToGivenUrlPostRequest, OptionalRedirectsToGivenUrlPostRequest):
    pass
