import requests

from insfetch.utils.funcs import get_proxies, cc_get

class ProfileHandler:
    _API_URL = 'https://www.instagram.com/api/v1/users/web_profile_info/'

    def __init__(self, username):
        self._username = username

        self._proxies = get_proxies()
        self._profile_dict = self._fetch_profile()

    @property
    def _headers(self):
        return {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'referer': f'https://www.instagram.com/{self._username}/',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'x-ig-app-id': '936619743392459',
            'x-requested-with': 'XMLHttpRequest',
        }

    @property
    def _params(self):
        return {'username': self._username}

    def _fetch_profile(self):
        result = requests.get(url=self._API_URL,
                              params=self._params,
                              headers=self._headers,
                              proxies = self._proxies)

        if (result_dict := result.json())['status'].lower() != 'ok':
            raise Exception('Unable to fetch profile data for "{self._username}"')

        return cc_get(result_dict, ['data', 'user'])

    @property
    def profile_dict(self):
        return self._profile_dict
