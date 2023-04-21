# TON Play Public API Connector Python

[![PyPI version](https://img.shields.io/pypi/v/tonplay-sdk)](https://pypi.python.org/pypi/tonplay-sdk)

This is a [lightweight library](https://github.com/ton-play/tonplay-python-sdk) that works as a connector to [TON Play public API](https://docs.tonplay.io/)
## Installation

```bash
pip install tonplay-sdk
```

## Get API Key

To get API Key [follow the link](https://docs.tonplay.io/digital-assets-api/api-key)

## RESTful APIs

Usage examples:
```python
from tonplay.methods import TonPlayApi

client = TonPlayApi(api_key='<YOUR API KEY>')

# Get assets on sale
print(client.get_assets_on_sale())
```

Please find `examples` folder to check for more endpoints.
- In order to set your API and Secret Key for use of the examples, create a file examples/config.ini with your keys.
- Eg:
```bash
# examples/config.ini
[keys]
api_key=abc123456
```
