
def get_user_assets(self, user_address):
    """
        Get assets belongs to user account

        GET /tondata/v2/assets/{address}

        Args:
            user_address (str) : user TON address

    """
    url_path = f"/tondata/v2/assets/{user_address}"
    return self.query(url_path)
