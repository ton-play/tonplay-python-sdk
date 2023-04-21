import uuid

from examples.utils.prepare_env import get_api_key
from tonplay.methods import TonPlayApi

client = TonPlayApi(api_key=get_api_key())

withdrawal_id = str(uuid.uuid4())
print(
    client.make_withdraw_request(withdrawal_id)
)