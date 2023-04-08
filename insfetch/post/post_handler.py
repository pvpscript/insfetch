import requests
import json

from insfetch.utils.funcs import get_proxies

class PostHandler:
    def __init__(self, post_id, post_page_parser):
        self._post_id = post_id
        self._post_page_parser = post_page_parser

        self._proxies = get_proxies()
        self._post_dict = self._fetch_post()
        
    def _build_post_url(self):
        return f'https://www.instagram.com/p/{self._post_id}/'

    def _fetch_post(self):
        data = requests.get(self._build_post_url(), proxies=self._proxies)

        if data.status_code != 200:
            raise Exception(f'Unable to fetch post with id "{self._post_id}"')

        self._post_page_parser.feed(data.text)
        return json.loads(self._post_page_parser.data)

    @property
    def post_dict(self):
        return self._post_dict
