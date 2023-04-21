from tonplay.lib.enums import AssetType
from tonplay.lib.utils import check_enum_parameter, check_ton_address


def get_assets_on_sale(self):
    """
    Get assets on sale by gameKey

    GET /market/v1/game/{gameKey}
    """

    url_path = f"/market/v1/game/{self._game_key}"
    return self.query(url_path)


def get_sft_market_depth(self, address):
    """
    Get same SFT on sale by asset address

    GET /market/v1/item/{address}

    Args:
        address (str): sft asset address

    """
    url_path = f"/market/v1/item/{address}"
    return self.query(url_path)


def put_on_sale(self, address, price, amount, type, seller_address):
    """
    Put asset on sale

    PUT /market/v1/sale

    Args:
        address (str)       : asset address
        price (float)       : the price in TON
        amount (int)        : amount of assets for sale ( 1 by default)
        type (str)          : AssetType ( NFT | SFT )
        seller_address (str) : seller address (asset's owner address)

    """
    check_enum_parameter(type, AssetType)
    check_ton_address(address, "address")
    check_ton_address(seller_address, "seller_address")

    url_path = f"/market/v1/sale"
    payload = {"address": address, "price": price, "amount": amount, "type": type, "sellerAddress": seller_address}
    return self.send_request("PUT", url_path, payload=payload)


def remove_from_sale(self, address, amount, type, seller_address):
    """
        Remove asset from sale

        DELETE /market/v1/sale

        Args:
            address (str)       : asset address
            amount (int)        : amount of assets for removing from sale ( 1 by default)
            type (str)          : AssetType ( NFT | SFT )
            seller_address (str) : seller address (asset's owner address)

        """
    check_enum_parameter(type, AssetType)
    check_ton_address(address, "address")
    check_ton_address(seller_address, "seller_address")

    url_path = f"/market/v1/sale"
    payload = {"address": address, "amount": amount, "type": type, "sellerAddress": seller_address}
    return self.send_request("DELETE", url_path, payload=payload)


def buy_asset(self, address, amount, type, seller_address, buyer_address):
    """
        Buy asset

        POST /market/v1/sale

        Args:
            address (str)       : asset address
            amount (int)        : amount of assets to buy ( 1 by default)
            type (str)          : AssetType ( NFT | SFT )
            seller_address (str) : seller address (asset's owner address)
            buyer_address (str) : buyer address

    """
    check_enum_parameter(type, AssetType)
    check_ton_address(address, "address")
    check_ton_address(seller_address, "seller_address")
    check_ton_address(seller_address, "buyer_address")

    url_path = f"/market/v1/sale"
    payload = {"address": address, "amount": amount, "type": type, "sellerAddress": seller_address, "buyerAddress": buyer_address}
    return self.send_request("POST", url_path, payload=payload)
