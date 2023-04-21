from tonplay.api import Api


class TonPlayApi(Api):
    def __init__(self, api_key, **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = "https://external.api.tonplay.io/x"
        super().__init__(api_key, **kwargs)

    # Market

    from tonplay.methods._market import get_assets_on_sale
    from tonplay.methods._market import get_sft_market_depth
    from tonplay.methods._market import put_on_sale
    from tonplay.methods._market import remove_from_sale
    from tonplay.methods._market import buy_asset

    # TON

    from tonplay.methods._ton import get_new_sft_tokens_mint_link
    from tonplay.methods._ton import get_nft_owner
    from tonplay.methods._ton import get_address_info
    from tonplay.methods._ton import get_burn_asset_link
    from tonplay.methods._ton import get_asset_transfer_link
    from tonplay.methods._ton import get_collectable_item_mint_link
    from tonplay.methods._ton import get_collection_deploy_link
    from tonplay.methods._ton import get_single_item_deploy_link

    # Games

    from tonplay.methods._game import make_withdraw_request

    # Auth

    from tonplay.methods._auth import check_tonplay_token

    # Assets

    from tonplay.methods._asset import get_user_assets

    # Users

    from tonplay.methods._user import get_user_by_identifier
    from tonplay.methods._user import get_users_by_identifiers
