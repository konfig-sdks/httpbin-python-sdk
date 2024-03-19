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

# Path params
QopSchema = schemas.StrSchema
UserSchema = schemas.StrSchema
PasswdSchema = schemas.StrSchema
AlgorithmSchema = schemas.StrSchema
StaleAfterSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'qop': typing.Union[QopSchema, str, ],
        'user': typing.Union[UserSchema, str, ],
        'passwd': typing.Union[PasswdSchema, str, ],
        'algorithm': typing.Union[AlgorithmSchema, str, ],
        'stale_after': typing.Union[StaleAfterSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_qop = api_client.PathParameter(
    name="qop",
    style=api_client.ParameterStyle.SIMPLE,
    schema=QopSchema,
    required=True,
)
request_path_user = api_client.PathParameter(
    name="user",
    style=api_client.ParameterStyle.SIMPLE,
    schema=UserSchema,
    required=True,
)
request_path_passwd = api_client.PathParameter(
    name="passwd",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PasswdSchema,
    required=True,
)
request_path_algorithm = api_client.PathParameter(
    name="algorithm",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AlgorithmSchema,
    required=True,
)
request_path_stale_after = api_client.PathParameter(
    name="stale_after",
    style=api_client.ParameterStyle.SIMPLE,
    schema=StaleAfterSchema,
    required=True,
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
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)


class BaseApi(api_client.Api):

    def _prompt_authorization_using_digest_mapped_args(
        self,
        qop: str,
        user: str,
        passwd: str,
        algorithm: str,
        stale_after: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if qop is not None:
            _path_params["qop"] = qop
        if user is not None:
            _path_params["user"] = user
        if passwd is not None:
            _path_params["passwd"] = passwd
        if algorithm is not None:
            _path_params["algorithm"] = algorithm
        if stale_after is not None:
            _path_params["stale_after"] = stale_after
        args.path = _path_params
        return args

    async def _aprompt_authorization_using_digest_oapg(
        self,
            path_params: typing.Optional[dict] = {},
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
        Prompts the user for authorization using Digest Auth + Algorithm.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_qop,
            request_path_user,
            request_path_passwd,
            request_path_algorithm,
            request_path_stale_after,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/digest-auth/{qop}/{user}/{passwd}/{algorithm}/{stale_after}',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
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


    def _prompt_authorization_using_digest_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Prompts the user for authorization using Digest Auth + Algorithm.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_qop,
            request_path_user,
            request_path_passwd,
            request_path_algorithm,
            request_path_stale_after,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/digest-auth/{qop}/{user}/{passwd}/{algorithm}/{stale_after}',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
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


class PromptAuthorizationUsingDigestRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aprompt_authorization_using_digest(
        self,
        qop: str,
        user: str,
        passwd: str,
        algorithm: str,
        stale_after: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._prompt_authorization_using_digest_mapped_args(
            qop=qop,
            user=user,
            passwd=passwd,
            algorithm=algorithm,
            stale_after=stale_after,
        )
        return await self._aprompt_authorization_using_digest_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def prompt_authorization_using_digest(
        self,
        qop: str,
        user: str,
        passwd: str,
        algorithm: str,
        stale_after: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._prompt_authorization_using_digest_mapped_args(
            qop=qop,
            user=user,
            passwd=passwd,
            algorithm=algorithm,
            stale_after=stale_after,
        )
        return self._prompt_authorization_using_digest_oapg(
            path_params=args.path,
        )

class PromptAuthorizationUsingDigest(BaseApi):

    async def aprompt_authorization_using_digest(
        self,
        qop: str,
        user: str,
        passwd: str,
        algorithm: str,
        stale_after: str,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aprompt_authorization_using_digest(
            qop=qop,
            user=user,
            passwd=passwd,
            algorithm=algorithm,
            stale_after=stale_after,
            **kwargs,
        )
    
    
    def prompt_authorization_using_digest(
        self,
        qop: str,
        user: str,
        passwd: str,
        algorithm: str,
        stale_after: str,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.prompt_authorization_using_digest(
            qop=qop,
            user=user,
            passwd=passwd,
            algorithm=algorithm,
            stale_after=stale_after,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        qop: str,
        user: str,
        passwd: str,
        algorithm: str,
        stale_after: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._prompt_authorization_using_digest_mapped_args(
            qop=qop,
            user=user,
            passwd=passwd,
            algorithm=algorithm,
            stale_after=stale_after,
        )
        return await self._aprompt_authorization_using_digest_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        qop: str,
        user: str,
        passwd: str,
        algorithm: str,
        stale_after: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._prompt_authorization_using_digest_mapped_args(
            qop=qop,
            user=user,
            passwd=passwd,
            algorithm=algorithm,
            stale_after=stale_after,
        )
        return self._prompt_authorization_using_digest_oapg(
            path_params=args.path,
        )

