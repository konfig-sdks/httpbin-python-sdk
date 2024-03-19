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

from . import path

# Query params
DurationSchema = schemas.NumberSchema
NumbytesSchema = schemas.IntSchema
CodeSchema = schemas.IntSchema
DelaySchema = schemas.NumberSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'duration': typing.Union[DurationSchema, decimal.Decimal, int, float, ],
        'numbytes': typing.Union[NumbytesSchema, decimal.Decimal, int, ],
        'code': typing.Union[CodeSchema, decimal.Decimal, int, ],
        'delay': typing.Union[DelaySchema, decimal.Decimal, int, float, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_duration = api_client.QueryParameter(
    name="duration",
    style=api_client.ParameterStyle.FORM,
    schema=DurationSchema,
    explode=True,
)
request_query_numbytes = api_client.QueryParameter(
    name="numbytes",
    style=api_client.ParameterStyle.FORM,
    schema=NumbytesSchema,
    explode=True,
)
request_query_code = api_client.QueryParameter(
    name="code",
    style=api_client.ParameterStyle.FORM,
    schema=CodeSchema,
    explode=True,
)
request_query_delay = api_client.QueryParameter(
    name="delay",
    style=api_client.ParameterStyle.FORM,
    schema=DelaySchema,
    explode=True,
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
_status_code_to_response = {
    '200': _response_for_200,
}


class BaseApi(api_client.Api):

    def _drip_data_over_duration_mapped_args(
        self,
        duration: typing.Optional[typing.Union[int, float]] = None,
        numbytes: typing.Optional[int] = None,
        code: typing.Optional[int] = None,
        delay: typing.Optional[typing.Union[int, float]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if duration is not None:
            _query_params["duration"] = duration
        if numbytes is not None:
            _query_params["numbytes"] = numbytes
        if code is not None:
            _query_params["code"] = code
        if delay is not None:
            _query_params["delay"] = delay
        args.query = _query_params
        return args

    async def _adrip_data_over_duration_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        Drips data over a duration after an optional initial delay.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_duration,
            request_query_numbytes,
            request_query_code,
            request_query_delay,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/drip',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _drip_data_over_duration_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Drips data over a duration after an optional initial delay.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_duration,
            request_query_numbytes,
            request_query_code,
            request_query_delay,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/drip',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            prefix_separator_iterator=prefix_separator_iterator,
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


class DripDataOverDurationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def adrip_data_over_duration(
        self,
        duration: typing.Optional[typing.Union[int, float]] = None,
        numbytes: typing.Optional[int] = None,
        code: typing.Optional[int] = None,
        delay: typing.Optional[typing.Union[int, float]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._drip_data_over_duration_mapped_args(
            duration=duration,
            numbytes=numbytes,
            code=code,
            delay=delay,
        )
        return await self._adrip_data_over_duration_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def drip_data_over_duration(
        self,
        duration: typing.Optional[typing.Union[int, float]] = None,
        numbytes: typing.Optional[int] = None,
        code: typing.Optional[int] = None,
        delay: typing.Optional[typing.Union[int, float]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._drip_data_over_duration_mapped_args(
            duration=duration,
            numbytes=numbytes,
            code=code,
            delay=delay,
        )
        return self._drip_data_over_duration_oapg(
            query_params=args.query,
        )

class DripDataOverDuration(BaseApi):

    async def adrip_data_over_duration(
        self,
        duration: typing.Optional[typing.Union[int, float]] = None,
        numbytes: typing.Optional[int] = None,
        code: typing.Optional[int] = None,
        delay: typing.Optional[typing.Union[int, float]] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.adrip_data_over_duration(
            duration=duration,
            numbytes=numbytes,
            code=code,
            delay=delay,
            **kwargs,
        )
    
    
    def drip_data_over_duration(
        self,
        duration: typing.Optional[typing.Union[int, float]] = None,
        numbytes: typing.Optional[int] = None,
        code: typing.Optional[int] = None,
        delay: typing.Optional[typing.Union[int, float]] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.drip_data_over_duration(
            duration=duration,
            numbytes=numbytes,
            code=code,
            delay=delay,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        duration: typing.Optional[typing.Union[int, float]] = None,
        numbytes: typing.Optional[int] = None,
        code: typing.Optional[int] = None,
        delay: typing.Optional[typing.Union[int, float]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._drip_data_over_duration_mapped_args(
            duration=duration,
            numbytes=numbytes,
            code=code,
            delay=delay,
        )
        return await self._adrip_data_over_duration_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        duration: typing.Optional[typing.Union[int, float]] = None,
        numbytes: typing.Optional[int] = None,
        code: typing.Optional[int] = None,
        delay: typing.Optional[typing.Union[int, float]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._drip_data_over_duration_mapped_args(
            duration=duration,
            numbytes=numbytes,
            code=code,
            delay=delay,
        )
        return self._drip_data_over_duration_oapg(
            query_params=args.query,
        )

