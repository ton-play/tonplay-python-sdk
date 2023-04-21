

def get_user_by_identifier(self, identifier):
    f"""
    Get info about TONPLAY user by identifier

    GET /auth/v1/user/identifier
    
    Args:
        identifier (str) : unique user id on TONPLAY
    """
    url_path = f"/auth/v1/user/{identifier}"
    return self.query(url_path)


def get_users_by_identifiers(self, identifiers_list):
    """
    Get info about TONPLAY users by their identifiers

    GET /auth/v1/user

    Args:
        identifiers_list [str] : list of unique users ids on TONPLAY

    """
    url_path = f"/auth/v1/user?identifiers=1"
    return self.query(url_path, identifiers=identifiers_list)
