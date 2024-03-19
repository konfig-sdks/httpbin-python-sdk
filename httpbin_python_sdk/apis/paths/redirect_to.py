from httpbin_python_sdk.paths.redirect_to.get import ApiForget
from httpbin_python_sdk.paths.redirect_to.put import ApiForput
from httpbin_python_sdk.paths.redirect_to.post import ApiForpost
from httpbin_python_sdk.paths.redirect_to.delete import ApiFordelete
from httpbin_python_sdk.paths.redirect_to.patch import ApiForpatch
from httpbin_python_sdk.paths.redirect_to.trace import ApiFortrace


class RedirectTo(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
    ApiForpatch,
    ApiFortrace,
):
    pass
