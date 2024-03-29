# coding: utf-8

"""
    httpbin.org

    A simple HTTP Request & Response Service.<br/> <br/> <b>Run locally: </b> <code>$ docker run -p 80:80 kennethreitz/httpbin</code>

    The version of the OpenAPI document: 0.9.2
    Contact: me@kennethreitz.org
    Created by: https://kennethreitz.org
"""

from httpbin_python_sdk.paths.absolute_redirect_n.get import AbsolutelyRedirectsN
from httpbin_python_sdk.paths.redirect_n.get import Call302RedirectsN
from httpbin_python_sdk.paths.redirect_to.put import GivenUrlPutRedirect
from httpbin_python_sdk.paths.relative_redirect_n.get import Relatively302RedirectsN
from httpbin_python_sdk.paths.redirect_to.delete import ToGivenUrlDelete
from httpbin_python_sdk.paths.redirect_to.get import ToGivenUrlGet
from httpbin_python_sdk.paths.redirect_to.patch import ToGivenUrlPatch
from httpbin_python_sdk.paths.redirect_to.post import ToGivenUrlPost
from httpbin_python_sdk.paths.redirect_to.trace import ToGivenUrlTrace
from httpbin_python_sdk.apis.tags.redirects_api_raw import RedirectsApiRaw


class RedirectsApi(
    AbsolutelyRedirectsN,
    Call302RedirectsN,
    GivenUrlPutRedirect,
    Relatively302RedirectsN,
    ToGivenUrlDelete,
    ToGivenUrlGet,
    ToGivenUrlPatch,
    ToGivenUrlPost,
    ToGivenUrlTrace,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: RedirectsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = RedirectsApiRaw(api_client)
