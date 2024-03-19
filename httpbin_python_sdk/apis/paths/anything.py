from httpbin_python_sdk.paths.anything.get import ApiForget
from httpbin_python_sdk.paths.anything.put import ApiForput
from httpbin_python_sdk.paths.anything.post import ApiForpost
from httpbin_python_sdk.paths.anything.delete import ApiFordelete
from httpbin_python_sdk.paths.anything.patch import ApiForpatch
from httpbin_python_sdk.paths.anything.trace import ApiFortrace


class Anything(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
    ApiForpatch,
    ApiFortrace,
):
    pass
