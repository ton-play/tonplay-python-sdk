
def check_tonplay_token(self, token):
    """
        Verify TONPLAY JWT token

        POST /auth/v1/check

        Args:
            token (str) : jwt token
    """
    url_path = "/auth/v1/check"
    return self.send_request("POST", url_path, token=token)
