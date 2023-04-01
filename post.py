import requests
import json

class Post:
    def __init__(self, post_id, post_parser):
        self._post_id = post_id
        self._post_parser = post_parser

    def _build_post_url(self):
        return f'https://www.instagram.com/p/{self._post_id}/'

    def fetch_post(self):
        data = requests.get(self._build_post_url())

        if data.status_code != 200:
            raise Exception(f'Unable to fetch post with id "{self._post_id}"')

        self._post_parser.feed(data.text)
        return json.loads(self._post_parser.data)
