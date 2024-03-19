# coding: utf-8

"""
    httpbin.org

    A simple HTTP Request & Response Service.<br/> <br/> <b>Run locally: </b> <code>$ docker run -p 80:80 kennethreitz/httpbin</code>

    The version of the OpenAPI document: 0.9.2
    Contact: me@kennethreitz.org
    Created by: https://kennethreitz.org
"""

from httpbin_python_sdk.paths.absolute_redirect_n.get import AbsolutelyRedirectsNRaw
from httpbin_python_sdk.paths.redirect_n.get import Call302RedirectsNRaw
from httpbin_python_sdk.paths.redirect_to.put import GivenUrlPutRedirectRaw
from httpbin_python_sdk.paths.relative_redirect_n.get import Relatively302RedirectsNRaw
from httpbin_python_sdk.paths.redirect_to.delete import ToGivenUrlDeleteRaw
from httpbin_python_sdk.paths.redirect_to.get import ToGivenUrlGetRaw
from httpbin_python_sdk.paths.redirect_to.patch import ToGivenUrlPatchRaw
from httpbin_python_sdk.paths.redirect_to.post import ToGivenUrlPostRaw
from httpbin_python_sdk.paths.redirect_to.trace import ToGivenUrlTraceRaw


class RedirectsApiRaw(
    AbsolutelyRedirectsNRaw,
    Call302RedirectsNRaw,
    GivenUrlPutRedirectRaw,
    Relatively302RedirectsNRaw,
    ToGivenUrlDeleteRaw,
    ToGivenUrlGetRaw,
    ToGivenUrlPatchRaw,
    ToGivenUrlPostRaw,
    ToGivenUrlTraceRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass