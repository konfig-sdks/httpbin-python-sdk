# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from httpbin_python_sdk.paths.digest_auth_qop_user_passwd import Api

from httpbin_python_sdk.paths import PathValues

path = PathValues.DIGESTAUTH_QOP_USER_PASSWD