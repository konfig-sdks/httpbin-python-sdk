import typing_extensions

from httpbin_python_sdk.apis.tags import TagValues
from httpbin_python_sdk.apis.tags.dynamic_data_api import DynamicDataApi
from httpbin_python_sdk.apis.tags.anything_api import AnythingApi
from httpbin_python_sdk.apis.tags.response_formats_api import ResponseFormatsApi
from httpbin_python_sdk.apis.tags.redirects_api import RedirectsApi
from httpbin_python_sdk.apis.tags.auth_api import AuthApi
from httpbin_python_sdk.apis.tags.status_codes_api import StatusCodesApi
from httpbin_python_sdk.apis.tags.http_methods_api import HTTPMethodsApi
from httpbin_python_sdk.apis.tags.response_inspection_api import ResponseInspectionApi
from httpbin_python_sdk.apis.tags.images_api import ImagesApi
from httpbin_python_sdk.apis.tags.cookies_api import CookiesApi
from httpbin_python_sdk.apis.tags.request_inspection_api import RequestInspectionApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DYNAMIC_DATA: DynamicDataApi,
        TagValues.ANYTHING: AnythingApi,
        TagValues.RESPONSE_FORMATS: ResponseFormatsApi,
        TagValues.REDIRECTS: RedirectsApi,
        TagValues.AUTH: AuthApi,
        TagValues.STATUS_CODES: StatusCodesApi,
        TagValues.HTTP_METHODS: HTTPMethodsApi,
        TagValues.RESPONSE_INSPECTION: ResponseInspectionApi,
        TagValues.IMAGES: ImagesApi,
        TagValues.COOKIES: CookiesApi,
        TagValues.REQUEST_INSPECTION: RequestInspectionApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DYNAMIC_DATA: DynamicDataApi,
        TagValues.ANYTHING: AnythingApi,
        TagValues.RESPONSE_FORMATS: ResponseFormatsApi,
        TagValues.REDIRECTS: RedirectsApi,
        TagValues.AUTH: AuthApi,
        TagValues.STATUS_CODES: StatusCodesApi,
        TagValues.HTTP_METHODS: HTTPMethodsApi,
        TagValues.RESPONSE_INSPECTION: ResponseInspectionApi,
        TagValues.IMAGES: ImagesApi,
        TagValues.COOKIES: CookiesApi,
        TagValues.REQUEST_INSPECTION: RequestInspectionApi,
    }
)
