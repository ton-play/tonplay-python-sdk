from examples.utils.prepare_env import get_api_key
from tonplay.methods import TonPlayApi

client = TonPlayApi(get_api_key())

# DEPLOY API

print(
    client.get_collection_deploy_link(
        # collection type (NFT | SFT)
        type="NFT",
        # collection owner address
        owner="",
        # collection metadata json url
        # https://docs.tonplay.io/digital-assets-api/metadata/assets-collection
        metadata_url="",
        # items common metadata url
        # for example: https://examplegame:5000/nfts
        common_metadata_url="",
        # royalty percent
        # for example: 1 (1%) , 2.5 (2.5%) etc
        royalty_percent=3.5,
        # royalty beneficiary address who will receive royalty
        royalty_beneficiary_address=""
    )
)

# mint new item from collection
print(
    client.get_collectable_item_mint_link(
        # collection address
        address="",
        # collection type (NFT | SFT)
        type="NFT",
        # new item owner address
        owner="",
        # last part of item metadata url
        # usually is filename.json
        # so finally collectionComonUrl + itemUrl = full link to item metadata
        item_metadata_url="10.json",
        # how many items will be mint
        amount=2
    )
)

# mint new SFT tokens
print(
    client.get_new_sft_tokens_mint_link(
        # SFT master contract (minter) address
        address="",
        # owner address of new minted tokens
        owner="",
        # how many tokens will be deployed (int)
        amount=100
    )
)

print(
    client.get_single_item_deploy_link(
        # asset type (NFT | SFT)
        type="NFT",
        # asset owner address
        owner="",
        # metadata json url
        # https://docs.tonplay.io/digital-assets-api/metadata/nft-assets
        metadata_url=""
    )
)
