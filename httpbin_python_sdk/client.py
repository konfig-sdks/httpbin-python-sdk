# coding: utf-8
"""
    httpbin.org

    A simple HTTP Request & Response Service.<br/> <br/> <b>Run locally: </b> <code>$ docker run -p 80:80 kennethreitz/httpbin</code>

    The version of the OpenAPI document: 0.9.2
    Contact: me@kennethreitz.org
    Created by: https://kennethreitz.org
"""

import typing
import inspect
from datetime import date, datetime
from httpbin_python_sdk.client_custom import ClientCustom
from httpbin_python_sdk.configuration import Configuration
from httpbin_python_sdk.api_client import ApiClient
from httpbin_python_sdk.type_util import copy_signature
from httpbin_python_sdk.apis.tags.anything_api import AnythingApi
from httpbin_python_sdk.apis.tags.auth_api import AuthApi
from httpbin_python_sdk.apis.tags.cookies_api import CookiesApi
from httpbin_python_sdk.apis.tags.dynamic_data_api import DynamicDataApi
from httpbin_python_sdk.apis.tags.http_methods_api import HTTPMethodsApi
from httpbin_python_sdk.apis.tags.images_api import ImagesApi
from httpbin_python_sdk.apis.tags.redirects_api import RedirectsApi
from httpbin_python_sdk.apis.tags.request_inspection_api import RequestInspectionApi
from httpbin_python_sdk.apis.tags.response_formats_api import ResponseFormatsApi
from httpbin_python_sdk.apis.tags.response_inspection_api import ResponseInspectionApi
from httpbin_python_sdk.apis.tags.status_codes_api import StatusCodesApi



class Httpbin(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.anything: AnythingApi = AnythingApi(api_client)
        self.auth: AuthApi = AuthApi(api_client)
        self.cookies: CookiesApi = CookiesApi(api_client)
        self.dynamic_data: DynamicDataApi = DynamicDataApi(api_client)
        self.http_methods: HTTPMethodsApi = HTTPMethodsApi(api_client)
        self.images: ImagesApi = ImagesApi(api_client)
        self.redirects: RedirectsApi = RedirectsApi(api_client)
        self.request_inspection: RequestInspectionApi = RequestInspectionApi(api_client)
        self.response_formats: ResponseFormatsApi = ResponseFormatsApi(api_client)
        self.response_inspection: ResponseInspectionApi = ResponseInspectionApi(api_client)
        self.status_codes: StatusCodesApi = StatusCodesApi(api_client)
