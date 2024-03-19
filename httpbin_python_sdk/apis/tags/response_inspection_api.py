# coding: utf-8

"""
    httpbin.org

    A simple HTTP Request & Response Service.<br/> <br/> <b>Run locally: </b> <code>$ docker run -p 80:80 kennethreitz/httpbin</code>

    The version of the OpenAPI document: 0.9.2
    Contact: me@kennethreitz.org
    Created by: https://kennethreitz.org
"""

from httpbin_python_sdk.paths.cache_value.get import CacheControlSet
from httpbin_python_sdk.paths.response_headers.post import GetResponseHeaders
from httpbin_python_sdk.paths.cache.get import NotModifiedGet
from httpbin_python_sdk.paths.response_headers.get import QueryHeadersGet
from httpbin_python_sdk.paths.etag_etag.get import ResourceInspectionGet
from httpbin_python_sdk.apis.tags.response_inspection_api_raw import ResponseInspectionApiRaw


class ResponseInspectionApi(
    CacheControlSet,
    GetResponseHeaders,
    NotModifiedGet,
    QueryHeadersGet,
    ResourceInspectionGet,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ResponseInspectionApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ResponseInspectionApiRaw(api_client)