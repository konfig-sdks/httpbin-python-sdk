from httpbin_python_sdk.paths.anything_anything.get import ApiForget
from httpbin_python_sdk.paths.anything_anything.put import ApiForput
from httpbin_python_sdk.paths.anything_anything.post import ApiForpost
from httpbin_python_sdk.paths.anything_anything.delete import ApiFordelete
from httpbin_python_sdk.paths.anything_anything.patch import ApiForpatch
from httpbin_python_sdk.paths.anything_anything.trace import ApiFortrace


class AnythingAnything(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
    ApiForpatch,
    ApiFortrace,
):
    pass
