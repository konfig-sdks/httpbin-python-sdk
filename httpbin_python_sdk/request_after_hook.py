# coding: utf-8

"""
    httpbin.org

    A simple HTTP Request & Response Service.<br/> <br/> <b>Run locally: </b> <code>$ docker run -p 80:80 kennethreitz/httpbin</code>

    The version of the OpenAPI document: 0.9.2
    Contact: me@kennethreitz.org
    Created by: https://kennethreitz.org
"""

import typing
from urllib3._collections import HTTPHeaderDict
from httpbin_python_sdk.configuration import Configuration

def request_after_hook(
        resource_path: str,
        method: str,
        configuration: Configuration,
        headers: typing.Optional[HTTPHeaderDict] = None,
        body: typing.Any = None,
        fields: typing.Optional[typing.Tuple[typing.Tuple[str, str], ...]] = None,
        auth_settings: typing.Optional[typing.List[str]] = None,
):
    pass