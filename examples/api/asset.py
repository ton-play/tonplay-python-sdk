from examples.utils.prepare_env import get_api_key
from tonplay.methods import TonPlayApi

client = TonPlayApi(get_api_key())

print(
    client.get_user_assets("EQBo5Rdhjl02oc1rAzwu_qxAWM6WCwxxUJckokyWEaYXG3xl")
)
