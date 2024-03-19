# coding: utf-8

"""
    httpbin.org

    A simple HTTP Request & Response Service.<br/> <br/> <b>Run locally: </b> <code>$ docker run -p 80:80 kennethreitz/httpbin</code>

    The version of the OpenAPI document: 0.9.2
    Contact: me@kennethreitz.org
    Created by: https://kennethreitz.org
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from httpbin_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from httpbin_python_sdk.api_response import AsyncGeneratorResponse
from httpbin_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from httpbin_python_sdk import schemas  # noqa: F401

from httpbin_python_sdk.model.redirects_to_given_url_post_request import RedirectsToGivenUrlPostRequest as RedirectsToGivenUrlPostRequestSchema
from httpbin_python_sdk.model.model_int import ModelInt as ModelIntSchema

from httpbin_python_sdk.type.model_int import ModelInt
from httpbin_python_sdk.type.redirects_to_given_url_post_request import RedirectsToGivenUrlPostRequest

from ...api_client import Dictionary
from httpbin_python_sdk.pydantic.redirects_to_given_url_post_request import RedirectsToGivenUrlPostRequest as RedirectsToGivenUrlPostRequestPydantic
from httpbin_python_sdk.pydantic.model_int import ModelInt as ModelIntPydantic

from . import path

# body param
SchemaForRequestBodyApplicationXWwwFormUrlencoded = RedirectsToGivenUrlPostRequestSchema


request_body_redirects_to_given_url_post_request = api_client.RequestBody(
    content={
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
    required=True,
)


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
)
_status_code_to_response = {
    'default': _response_for_default,
}


class BaseApi(api_client.Api):

    def _given_url_put_redirect_mapped_args(
        self,
        url: str,
        status_code: typing.Optional[ModelInt] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if url is not None:
            _body["url"] = url
        if status_code is not None:
            _body["status_code"] = status_code
        args.body = _body
        return args

    async def _agiven_url_put_redirect_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        302/3XX Redirects to the given URL.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/redirect-to',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_redirects_to_given_url_post_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _given_url_put_redirect_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        302/3XX Redirects to the given URL.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/redirect-to',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_redirects_to_given_url_post_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GivenUrlPutRedirectRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def agiven_url_put_redirect(
        self,
        url: str,
        status_code: typing.Optional[ModelInt] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._given_url_put_redirect_mapped_args(
            url=url,
            status_code=status_code,
        )
        return await self._agiven_url_put_redirect_oapg(
            body=args.body,
            **kwargs,
        )
    
    def given_url_put_redirect(
        self,
        url: str,
        status_code: typing.Optional[ModelInt] = None,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._given_url_put_redirect_mapped_args(
            url=url,
            status_code=status_code,
        )
        return self._given_url_put_redirect_oapg(
            body=args.body,
        )

class GivenUrlPutRedirect(BaseApi):

    async def agiven_url_put_redirect(
        self,
        url: str,
        status_code: typing.Optional[ModelInt] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.agiven_url_put_redirect(
            url=url,
            status_code=status_code,
            **kwargs,
        )
    
    
    def given_url_put_redirect(
        self,
        url: str,
        status_code: typing.Optional[ModelInt] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.given_url_put_redirect(
            url=url,
            status_code=status_code,
        )


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        url: str,
        status_code: typing.Optional[ModelInt] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._given_url_put_redirect_mapped_args(
            url=url,
            status_code=status_code,
        )
        return await self._agiven_url_put_redirect_oapg(
            body=args.body,
            **kwargs,
        )
    
    def put(
        self,
        url: str,
        status_code: typing.Optional[ModelInt] = None,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._given_url_put_redirect_mapped_args(
            url=url,
            status_code=status_code,
        )
        return self._given_url_put_redirect_oapg(
            body=args.body,
        )

