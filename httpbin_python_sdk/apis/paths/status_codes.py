from httpbin_python_sdk.paths.status_codes.get import ApiForget
from httpbin_python_sdk.paths.status_codes.put import ApiForput
from httpbin_python_sdk.paths.status_codes.post import ApiForpost
from httpbin_python_sdk.paths.status_codes.delete import ApiFordelete
from httpbin_python_sdk.paths.status_codes.patch import ApiForpatch
from httpbin_python_sdk.paths.status_codes.trace import ApiFortrace


class StatusCodes(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
    ApiForpatch,
    ApiFortrace,
):
    pass
