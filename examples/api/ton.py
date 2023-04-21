from examples.utils.prepare_env import get_api_key
from tonplay.methods import TonPlayApi

client = TonPlayApi(get_api_key())

print(
    client.get_nft_owner("EQCWxV31UgGZZcnuKoGYnY6LlxE7stVZ1kXIRaML1N3fIHgF")
)

print(
    client.get_address_info("EQCWxV31UgGZZcnuKoGYnY6LlxE7stVZ1kXIRaML1N3fIHgF")
)

print(
    client.get_burn_asset_link(
        # asset to burn
        address="",
        # asset type
        type="NFT",
        # amount (default=1)
        amount=None,
        # current owner address
        owner_address=""
    )
)

print(
    client.get_asset_transfer_link(
        # asset to transfer
        address="",
        # asset type
        type="NFT",
        # amount (default=1)
        amount=None,
        # current owner address
        current_owner="",
        # new owner address
        new_owner=""
    )
)
