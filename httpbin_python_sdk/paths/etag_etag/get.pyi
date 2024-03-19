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



from ...api_client import Dictionary

# Header params
IfNoneMatchSchema = schemas.StrSchema
IfMatchSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'If-None-Match': typing.Union[IfNoneMatchSchema, str, ],
        'If-Match': typing.Union[IfMatchSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_if_none_match = api_client.HeaderParameter(
    name="If-None-Match",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IfNoneMatchSchema,
)
request_header_if_match = api_client.HeaderParameter(
    name="If-Match",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IfMatchSchema,
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
)


@dataclass
class ApiResponseFor412(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor412Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_412 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor412,
    response_cls_async=ApiResponseFor412Async,
)


class BaseApi(api_client.Api):

    def _resource_inspection_get_mapped_args(
        self,
        if_none_match: typing.Optional[str] = None,
        if_match: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        if if_none_match is not None:
            _header_params["If-None-Match"] = if_none_match
        if if_match is not None:
            _header_params["If-Match"] = if_match
        args.header = _header_params
        return args

    async def _aresource_inspection_get_oapg(
        self,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Assumes the resource has the given etag and responds to If-None-Match and If-Match headers appropriately.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_if_none_match,
            request_header_if_match,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/etag/{etag}',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
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


    def _resource_inspection_get_oapg(
        self,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Assumes the resource has the given etag and responds to If-None-Match and If-Match headers appropriately.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_if_none_match,
            request_header_if_match,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/etag/{etag}',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ResourceInspectionGetRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aresource_inspection_get(
        self,
        if_none_match: typing.Optional[str] = None,
        if_match: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._resource_inspection_get_mapped_args(
            if_none_match=if_none_match,
            if_match=if_match,
        )
        return await self._aresource_inspection_get_oapg(
            header_params=args.header,
            **kwargs,
        )
    
    def resource_inspection_get(
        self,
        if_none_match: typing.Optional[str] = None,
        if_match: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._resource_inspection_get_mapped_args(
            if_none_match=if_none_match,
            if_match=if_match,
        )
        return self._resource_inspection_get_oapg(
            header_params=args.header,
        )

class ResourceInspectionGet(BaseApi):

    async def aresource_inspection_get(
        self,
        if_none_match: typing.Optional[str] = None,
        if_match: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aresource_inspection_get(
            if_none_match=if_none_match,
            if_match=if_match,
            **kwargs,
        )
    
    
    def resource_inspection_get(
        self,
        if_none_match: typing.Optional[str] = None,
        if_match: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.resource_inspection_get(
            if_none_match=if_none_match,
            if_match=if_match,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        if_none_match: typing.Optional[str] = None,
        if_match: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._resource_inspection_get_mapped_args(
            if_none_match=if_none_match,
            if_match=if_match,
        )
        return await self._aresource_inspection_get_oapg(
            header_params=args.header,
            **kwargs,
        )
    
    def get(
        self,
        if_none_match: typing.Optional[str] = None,
        if_match: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._resource_inspection_get_mapped_args(
            if_none_match=if_none_match,
            if_match=if_match,
        )
        return self._resource_inspection_get_oapg(
            header_params=args.header,
        )

