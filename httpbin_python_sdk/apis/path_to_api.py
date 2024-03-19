import typing_extensions

from httpbin_python_sdk.paths import PathValues
from httpbin_python_sdk.apis.paths.absolute_redirect_n import AbsoluteRedirectN
from httpbin_python_sdk.apis.paths.anything import Anything
from httpbin_python_sdk.apis.paths.anything_anything import AnythingAnything
from httpbin_python_sdk.apis.paths.base64_value import Base64Value
from httpbin_python_sdk.apis.paths.basic_auth_user_passwd import BasicAuthUserPasswd
from httpbin_python_sdk.apis.paths.bearer import Bearer
from httpbin_python_sdk.apis.paths.brotli import Brotli
from httpbin_python_sdk.apis.paths.bytes_n import BytesN
from httpbin_python_sdk.apis.paths.cache import Cache
from httpbin_python_sdk.apis.paths.cache_value import CacheValue
from httpbin_python_sdk.apis.paths.cookies import Cookies
from httpbin_python_sdk.apis.paths.cookies_delete import CookiesDelete
from httpbin_python_sdk.apis.paths.cookies_set import CookiesSet
from httpbin_python_sdk.apis.paths.cookies_set_name_value import CookiesSetNameValue
from httpbin_python_sdk.apis.paths.deflate import Deflate
from httpbin_python_sdk.apis.paths.delay_delay import DelayDelay
from httpbin_python_sdk.apis.paths.delete import Delete
from httpbin_python_sdk.apis.paths.deny import Deny
from httpbin_python_sdk.apis.paths.digest_auth_qop_user_passwd import DigestAuthQopUserPasswd
from httpbin_python_sdk.apis.paths.digest_auth_qop_user_passwd_algorithm import DigestAuthQopUserPasswdAlgorithm
from httpbin_python_sdk.apis.paths.digest_auth_qop_user_passwd_algorithm_stale_after import DigestAuthQopUserPasswdAlgorithmStaleAfter
from httpbin_python_sdk.apis.paths.drip import Drip
from httpbin_python_sdk.apis.paths.encoding_utf8 import EncodingUtf8
from httpbin_python_sdk.apis.paths.etag_etag import EtagEtag
from httpbin_python_sdk.apis.paths.get import Get
from httpbin_python_sdk.apis.paths.gzip import Gzip
from httpbin_python_sdk.apis.paths.headers import Headers
from httpbin_python_sdk.apis.paths.hidden_basic_auth_user_passwd import HiddenBasicAuthUserPasswd
from httpbin_python_sdk.apis.paths.html import Html
from httpbin_python_sdk.apis.paths.image import Image
from httpbin_python_sdk.apis.paths.image_jpeg import ImageJpeg
from httpbin_python_sdk.apis.paths.image_png import ImagePng
from httpbin_python_sdk.apis.paths.image_svg import ImageSvg
from httpbin_python_sdk.apis.paths.image_webp import ImageWebp
from httpbin_python_sdk.apis.paths.ip import Ip
from httpbin_python_sdk.apis.paths.json import Json
from httpbin_python_sdk.apis.paths.links_n_offset import LinksNOffset
from httpbin_python_sdk.apis.paths.patch import Patch
from httpbin_python_sdk.apis.paths.post import Post
from httpbin_python_sdk.apis.paths.put import Put
from httpbin_python_sdk.apis.paths.range_numbytes import RangeNumbytes
from httpbin_python_sdk.apis.paths.redirect_to import RedirectTo
from httpbin_python_sdk.apis.paths.redirect_n import RedirectN
from httpbin_python_sdk.apis.paths.relative_redirect_n import RelativeRedirectN
from httpbin_python_sdk.apis.paths.response_headers import ResponseHeaders
from httpbin_python_sdk.apis.paths.robots_txt import RobotsTxt
from httpbin_python_sdk.apis.paths.status_codes import StatusCodes
from httpbin_python_sdk.apis.paths.stream_bytes_n import StreamBytesN
from httpbin_python_sdk.apis.paths.stream_n import StreamN
from httpbin_python_sdk.apis.paths.user_agent import UserAgent
from httpbin_python_sdk.apis.paths.uuid import Uuid
from httpbin_python_sdk.apis.paths.xml import Xml

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ABSOLUTEREDIRECT_N: AbsoluteRedirectN,
        PathValues.ANYTHING: Anything,
        PathValues.ANYTHING_ANYTHING: AnythingAnything,
        PathValues.BASE64_VALUE: Base64Value,
        PathValues.BASICAUTH_USER_PASSWD: BasicAuthUserPasswd,
        PathValues.BEARER: Bearer,
        PathValues.BROTLI: Brotli,
        PathValues.BYTES_N: BytesN,
        PathValues.CACHE: Cache,
        PathValues.CACHE_VALUE: CacheValue,
        PathValues.COOKIES: Cookies,
        PathValues.COOKIES_DELETE: CookiesDelete,
        PathValues.COOKIES_SET: CookiesSet,
        PathValues.COOKIES_SET_NAME_VALUE: CookiesSetNameValue,
        PathValues.DEFLATE: Deflate,
        PathValues.DELAY_DELAY: DelayDelay,
        PathValues.DELETE: Delete,
        PathValues.DENY: Deny,
        PathValues.DIGESTAUTH_QOP_USER_PASSWD: DigestAuthQopUserPasswd,
        PathValues.DIGESTAUTH_QOP_USER_PASSWD_ALGORITHM: DigestAuthQopUserPasswdAlgorithm,
        PathValues.DIGESTAUTH_QOP_USER_PASSWD_ALGORITHM_STALE_AFTER: DigestAuthQopUserPasswdAlgorithmStaleAfter,
        PathValues.DRIP: Drip,
        PathValues.ENCODING_UTF8: EncodingUtf8,
        PathValues.ETAG_ETAG: EtagEtag,
        PathValues.GET: Get,
        PathValues.GZIP: Gzip,
        PathValues.HEADERS: Headers,
        PathValues.HIDDENBASICAUTH_USER_PASSWD: HiddenBasicAuthUserPasswd,
        PathValues.HTML: Html,
        PathValues.IMAGE: Image,
        PathValues.IMAGE_JPEG: ImageJpeg,
        PathValues.IMAGE_PNG: ImagePng,
        PathValues.IMAGE_SVG: ImageSvg,
        PathValues.IMAGE_WEBP: ImageWebp,
        PathValues.IP: Ip,
        PathValues.JSON: Json,
        PathValues.LINKS_N_OFFSET: LinksNOffset,
        PathValues.PATCH: Patch,
        PathValues.POST: Post,
        PathValues.PUT: Put,
        PathValues.RANGE_NUMBYTES: RangeNumbytes,
        PathValues.REDIRECTTO: RedirectTo,
        PathValues.REDIRECT_N: RedirectN,
        PathValues.RELATIVEREDIRECT_N: RelativeRedirectN,
        PathValues.RESPONSEHEADERS: ResponseHeaders,
        PathValues.ROBOTS_TXT: RobotsTxt,
        PathValues.STATUS_CODES: StatusCodes,
        PathValues.STREAMBYTES_N: StreamBytesN,
        PathValues.STREAM_N: StreamN,
        PathValues.USERAGENT: UserAgent,
        PathValues.UUID: Uuid,
        PathValues.XML: Xml,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ABSOLUTEREDIRECT_N: AbsoluteRedirectN,
        PathValues.ANYTHING: Anything,
        PathValues.ANYTHING_ANYTHING: AnythingAnything,
        PathValues.BASE64_VALUE: Base64Value,
        PathValues.BASICAUTH_USER_PASSWD: BasicAuthUserPasswd,
        PathValues.BEARER: Bearer,
        PathValues.BROTLI: Brotli,
        PathValues.BYTES_N: BytesN,
        PathValues.CACHE: Cache,
        PathValues.CACHE_VALUE: CacheValue,
        PathValues.COOKIES: Cookies,
        PathValues.COOKIES_DELETE: CookiesDelete,
        PathValues.COOKIES_SET: CookiesSet,
        PathValues.COOKIES_SET_NAME_VALUE: CookiesSetNameValue,
        PathValues.DEFLATE: Deflate,
        PathValues.DELAY_DELAY: DelayDelay,
        PathValues.DELETE: Delete,
        PathValues.DENY: Deny,
        PathValues.DIGESTAUTH_QOP_USER_PASSWD: DigestAuthQopUserPasswd,
        PathValues.DIGESTAUTH_QOP_USER_PASSWD_ALGORITHM: DigestAuthQopUserPasswdAlgorithm,
        PathValues.DIGESTAUTH_QOP_USER_PASSWD_ALGORITHM_STALE_AFTER: DigestAuthQopUserPasswdAlgorithmStaleAfter,
        PathValues.DRIP: Drip,
        PathValues.ENCODING_UTF8: EncodingUtf8,
        PathValues.ETAG_ETAG: EtagEtag,
        PathValues.GET: Get,
        PathValues.GZIP: Gzip,
        PathValues.HEADERS: Headers,
        PathValues.HIDDENBASICAUTH_USER_PASSWD: HiddenBasicAuthUserPasswd,
        PathValues.HTML: Html,
        PathValues.IMAGE: Image,
        PathValues.IMAGE_JPEG: ImageJpeg,
        PathValues.IMAGE_PNG: ImagePng,
        PathValues.IMAGE_SVG: ImageSvg,
        PathValues.IMAGE_WEBP: ImageWebp,
        PathValues.IP: Ip,
        PathValues.JSON: Json,
        PathValues.LINKS_N_OFFSET: LinksNOffset,
        PathValues.PATCH: Patch,
        PathValues.POST: Post,
        PathValues.PUT: Put,
        PathValues.RANGE_NUMBYTES: RangeNumbytes,
        PathValues.REDIRECTTO: RedirectTo,
        PathValues.REDIRECT_N: RedirectN,
        PathValues.RELATIVEREDIRECT_N: RelativeRedirectN,
        PathValues.RESPONSEHEADERS: ResponseHeaders,
        PathValues.ROBOTS_TXT: RobotsTxt,
        PathValues.STATUS_CODES: StatusCodes,
        PathValues.STREAMBYTES_N: StreamBytesN,
        PathValues.STREAM_N: StreamN,
        PathValues.USERAGENT: UserAgent,
        PathValues.UUID: Uuid,
        PathValues.XML: Xml,
    }
)
