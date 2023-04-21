from tonplay.lib.enums import AssetType
from tonplay.lib.utils import check_ton_address, check_enum_parameter


def get_nft_owner(self, address):
    """
        Get NFT owner's address

        GET /tondata/v1/ton/{address}/owner

        Args:
            address (str): NFT address
        """
    check_ton_address(address, "address")
    url_path = f"/tondata/v1/ton/{address}/owner"
    return self.query(url_path)


def get_address_info(self, address):
    """
        Get information about contract

        GET /tondata/v1/ton/{address}/status

        Args:
            address (str): contract address
        """
    check_ton_address(address, "address")
    url_path = f"/tondata/v1/ton/{address}/status"
    return self.query(url_path)


def get_burn_asset_link(self, address, amount, type, owner_address):
    """
        Burn selected asset

        DELETE /tondata/v1/ton/burn/{address}

        Args:
            address (str)   : asset address to burn
            type (str)      : AssetType ( NFT | SFT )
            amount (int)    : asset amount to burn (for SFT) default 1
            owner_address   : asset's owner
    """
    check_ton_address(address, "address")
    check_enum_parameter(type, AssetType)
    url_path = f"/tondata/v1/ton/burn/{address}"
    payload = {"amount": amount, "ownerAddress": owner_address, "type": type}
    return self.send_request("DELETE", url_path, payload=payload)


def get_asset_transfer_link(self, address, amount, type, current_owner, new_owner):
    """
        Generate link to transfer asset

        POST /tondata/v1/ton/transfer/{address}

        Args:
            address (str)   : asset address to burn
            type (str)      : AssetType ( NFT | SFT )
            amount (int)    : asset amount to burn (for SFT) default 1
            current_owner   : current asset's owner
            new_owner       : new asset's owner

    """
    check_ton_address(address, "address")
    check_ton_address(current_owner, "current_owner")
    check_ton_address(new_owner, "new_owner")
    check_enum_parameter(type, AssetType)
    url_path = f"/tondata/v1/ton/transfer/{address}"
    payload = {"amount": amount, "newOwner": new_owner, "currentOwnerAddress": current_owner, "type": type}
    return self.send_request("POST", url_path, payload=payload)


def get_collection_deploy_link(
        self,
        type,
        owner,
        metadata_url,
        common_metadata_url,
        royalty_percent,
        royalty_beneficiary_address
):
    """
        Generate link to deploy collection

        POST /tondata/v1/ton/deploy/collection

        Args:
            type (str)                          : AssetType ( NFT | SFT )
            owner (str)                         : who will be asset's owner
            metadata_url (str)                  : collection metadata url
            common_metadata_url (str)           : common item medata url
            royalty_percent (float)             : royalty percent (e.g. 1.5 , 2 , 4.5 )
            royalty_beneficiary_address (str)   : royalty recipient address

    """
    check_ton_address(owner, "owner")
    check_ton_address(royalty_beneficiary_address, "royalty_beneficiary_address")
    check_enum_parameter(type, AssetType)
    url_path = f"/tondata/v1/ton/deploy/collection"

    denominator = pow(10, len(str(float(royalty_percent)).split(".")[1]))
    numerator = royalty_percent * denominator
    payload = {
        "owner": owner,
        "maxSupply": 0,
        "collectionMetadataUrl": metadata_url,
        "itemMetadataCommonUrl": common_metadata_url,
        "royalty": {
            "numerator": numerator,
            "denominator": denominator,
            "beneficiaryAddress": royalty_beneficiary_address
        }
    }
    return self.send_request("POST", url_path, payload=payload, type=type)


def get_single_item_deploy_link(
        self,
        type,
        owner,
        metadata_url
):
    """
        Generate link to deploy single asset

        POST /tondata/v1/ton/deploy/single

        Args:
            type (str)                          : AssetType ( NFT | SFT )
            owner (str)                         : who will be asset's owner
            metadata_url (str)                  : collection metadata url

    """
    check_ton_address(owner, "owner")
    check_enum_parameter(type, AssetType)
    url_path = f"/tondata/v1/ton/deploy/single"
    payload = {
        "owner": owner,
        "maxSupply": 0,
        "metadata": metadata_url,
    }
    return self.send_request("POST", url_path, payload=payload, type=type)


def get_collectable_item_mint_link(
        self,
        address,
        type,
        owner,
        item_metadata_url,
        amount
):
    """
        Generate link to mint new collectable item

        POST /tondata/v1/ton/mint/collection/{address}

        Args:
            type (str)                          : AssetType ( NFT | SFT )
            address (str)                       : collection address
            owner (str)                         : who will be asset's owner
            item_metadata_url (str)             : item metadata part url
            amount (int)                        : how many collectables need to be deployed

    """
    check_ton_address(owner, "owner")
    check_ton_address(address, "address")
    check_enum_parameter(type, AssetType)
    url_path = f"/tondata/v1/ton/mint/collection/{address}"
    payload = {
        "owner": owner,
        "itemMetadataPartOfUrl": item_metadata_url,
        "amount": amount,
    }
    return self.send_request("POST", url_path, payload=payload, type=type)


def get_new_sft_tokens_mint_link(
        self,
        address,
        owner,
        amount
):
    """
        Generate link to mint new SFT tokens

        POST /tondata/v1/ton/mint/sft/{address}

        Args:
            address (str)                       : collection address
            owner (str)                         : who will be asset's owner
            amount (int)                        : how many collectables need to be deployed

    """
    check_ton_address(owner, "owner")
    check_ton_address(address, "address")
    url_path = f"/tondata/v1/ton/mint/sft/{address}"
    payload = {
        "owner": owner,
        "amount": amount,
    }
    return self.send_request("POST", url_path, payload=payload)
