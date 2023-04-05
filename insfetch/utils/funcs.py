import os
import sys

def chained_get(dict_data, chain):
    if dict_data is None or len(chain) < 1:
        return None

    if len(chain) == 1:
        return dict_data.get(chain[0])

    return chained_get(dict_data.get(chain.pop(0)), chain)

def get_proxies():
    metadata = {
        'http': 'INSFETCH_HTTP_PROXY',
        'https': 'INSFETCH_HTTPS_PROXY',
    }

    return {protocol: address
            for protocol, env_key in metadata.items()
            if (address := os.environ.get(env_key)) is not None}
