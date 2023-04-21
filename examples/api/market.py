from examples.utils.prepare_env import get_api_key
from tonplay.methods import TonPlayApi

client = TonPlayApi(api_key=get_api_key())

print(
    client.get_assets_on_sale()
)

print(
    client.get_sft_market_depth("EQA4R4qC__ogFwb_27vYQ4Y8Lyg_N4K4Rb2RaGWxnwj2x4Ya")
)

print(
    client.put_on_sale(
        # asset address
        address="",
        # price in TON
        price=10,
        # amount (for SFT) by default = 1
        amount=1,
        # type
        type='SFT',
        # seller address = current owner address
        seller_address=""
    )
)

print(
    client.remove_from_sale(
        # asset address
        address="",
        # amount for remove (for SFT) by default = 1
        amount=1,
        # type
        type='SFT',
        # seller address = current owner address
        seller_address=""
    )
)

print(
    client.buy_asset(
        # asset address
        address="",
        # amount for remove (for SFT) by default = 1
        amount=1,
        # type
        type='SFT',
        # seller address = who is selling
        seller_address="",
        # buyer address = who is buying right now
        buyer_address=""
    )
)
