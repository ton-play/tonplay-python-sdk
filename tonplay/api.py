import json
import logging
from json import JSONDecodeError

import requests

from .__version__ import __version__
from .error import ClientError, ServerError, ParameterArgumentError


class Api(object):
    """API base class
        Keyword Args:
            base_url (str, optional): the API base url. By default, it's https://external.api.tonplay.io/x
    """

    def _validate_api_key(self, api_key):
        if len(api_key) != 31:
            raise ParameterArgumentError("wrong api_key length")
        decomposed = api_key.split(":")
        if len(decomposed) != 2:
            raise ParameterArgumentError("wrong api_key format")

    def __init__(
            self,
            api_key=None,
            base_url=None
    ):
        self._validate_api_key(api_key)
        self.api_key = api_key
        self.base_url = base_url

        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json",
                "User-Agent": "tonplay-connector/" + __version__,
                "X-Auth-Tonplay": api_key,
            }
        )
        self._logger = logging.getLogger(__name__)
        self._game_key = api_key.split(":")[0]

        return

    def query(self, url_path, **kwargs):
        return self.send_request("GET", url_path, **kwargs)

    def send_request(self, http_method, url_path, payload=None, **kwargs):
        if payload is None:
            payload = {}

        url = self.base_url + url_path
        self._logger.debug("url: " + url)
        params = {
            "url": url,
            "params": kwargs
        }
        if http_method != "GET":
            params["data"] = json.dumps(payload)

        response = self._dispatch_request(http_method)(**params)
        self._logger.debug("raw response from server:" + response.text)
        self._handle_exception(response)

        try:
            data = response.json()
        except ValueError:
            data = response.text
        result = {}

        if len(result) != 0:
            result["data"] = data
            return result

        return data

    def _dispatch_request(self, http_method):
        return {
            "GET": self.session.get,
            "DELETE": self.session.delete,
            "PUT": self.session.put,
            "POST": self.session.post,
        }.get(http_method, "GET")

    def _handle_exception(self, response):
        status_code = response.status_code
        # print(response.text)
        if status_code < 400:
            return
        if 400 <= status_code < 500:
            try:
                err = json.loads(response.text)
            except JSONDecodeError:
                raise ClientError(
                    status_code, None, response.text, None, response.headers
                )
            error_data = None
            if "timestamp" in err:
                error_data = {
                    "type": err["error"],
                    "message": err["message"]
                }
            else:
                error_data = err["error"]
            raise ClientError(
                status_code, error_data["type"], error_data["message"], response.headers
            )
        raise ServerError(status_code, response.text)
