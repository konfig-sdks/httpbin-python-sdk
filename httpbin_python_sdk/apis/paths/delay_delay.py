from httpbin_python_sdk.paths.delay_delay.get import ApiForget
from httpbin_python_sdk.paths.delay_delay.put import ApiForput
from httpbin_python_sdk.paths.delay_delay.post import ApiForpost
from httpbin_python_sdk.paths.delay_delay.delete import ApiFordelete
from httpbin_python_sdk.paths.delay_delay.patch import ApiForpatch
from httpbin_python_sdk.paths.delay_delay.trace import ApiFortrace


class DelayDelay(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
    ApiForpatch,
    ApiFortrace,
):
    pass
