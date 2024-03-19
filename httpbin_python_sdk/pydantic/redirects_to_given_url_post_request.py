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
from pydantic import BaseModel, Field, RootModel

from httpbin_python_sdk.pydantic.model_int import ModelInt

class RedirectsToGivenUrlPostRequest(BaseModel):
    url: str = Field(alias='url')

    status_code: typing.Optional[ModelInt] = Field(None, alias='status_code')
    class Config:
        arbitrary_types_allowed = True
