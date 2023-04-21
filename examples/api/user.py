from examples.utils.prepare_env import get_api_key
from tonplay.methods import TonPlayApi

client = TonPlayApi(get_api_key())
print(
    client.get_user_by_identifier("01cf820f-b173-327f-a0e4-3e72feb1c4b8")
)

print(
    client.get_users_by_identifiers([
        "d9931e3566e3b0e2fd846def9bfde53f7f6416c314d85fc9c98c69d04aa37275",
        "6b5283ab-d100-3c5b-8ad7-091c08282e70"
    ])
)
