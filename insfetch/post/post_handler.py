import requests
import json

from insfetch.core.utils import chained_get
from insfetch.core.utils import get_proxies 
from insfetch.post.content.image import Image

class PostHandler:
    _post_dict = None

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

    # TODO: code below needs refactoring!

    def article_body(self): # [root]
        return chained_get(self._post_dict, ['articleBody'])

    @property
    def image(self):
        return Image(self._post_dict['image'])

    def num_videos(self): # video
        pass

    def video_dimensions(self, index): # video
        pass

    def video_url(self, index): # video
        pass

    def video_thumbnail(self, index): # video
        pass

    def video_upload_date(self, index): # video
        pass

    def video_likes(self, index): # video
        pass

    def author_username(self): # author
        return chained_get(self._post_dict, ['author', 'identifier', 'value'])

    def author_name(self): # author
        return chained_get(self._post_dict, ['author', 'name'])

    def author_image(self): # author
        return chained_get(self._post_dict, ['author', 'image'])

    def num_comments(self): # interactionStatistic
        pass

    def num_likes(self): # interactionStatistic
        pass

    def top_comment(self): # comment
        pass

    def top_comment_author_name(self): # comment
        pass

    def top_comment_author_username(self): # comment
        pass

    def top_comment_author_image(self): # comment
        pass

    def content_location(self): # [root]
        pass

    def creation_date(self): # [root]
        pass

    def modification_date(self): # [root]
        pass