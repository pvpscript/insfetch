import requests
import json

class PostHandler:
    _post_dict = None

    def __init__(self, post_id, post_page_parser):
        self._post_id = post_id
        self._post_page_parser = post_page_parser

        self._post_dict = self._fetch_post()

    def _build_post_url(self):
        return f'https://www.instagram.com/p/{self._post_id}/'

    def _fetch_post(self):
        data = requests.get(self._build_post_url())

        if data.status_code != 200:
            raise Exception(f'Unable to fetch post with id "{self._post_id}"')

        self._post_page_parser.feed(data.text)
        return json.loads(self._post_page_parser.data)

    def _get(self, dict_data, chain):
        if dict_data is None or len(chain) < 1:
            return None

        if len(chain) == 1:
            return dict_data.get(chain[0])

        return self._get(dict_data.get(chain.pop(0)), chain)

    # TODO: code below needs refactoring!

    def article_body(self): # [root]
        return self._get(self._post_dict, ['articleBody'])

    def images(self): # [root]
        pass # amount of images, dimensions, url, caption

    def videos(self): # [root]
        pass # amount of videos, dimensions, content url, thumbnail url, upload date, num of likes

    def author_username(self): # author
        return self._get(self._post_dict, ['author', 'identifier', 'value'])

    def author_name(self): # author
        return self._get(self._post_dict, ['author', 'name'])

    def author_image(self): # author
        return self._get(self._post_dict, ['author', 'image'])

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
