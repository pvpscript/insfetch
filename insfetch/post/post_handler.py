import requests
import json

from insfetch.post.content.image import Image
from insfetch.post.content.video import Video
from insfetch.post.content.author import Author
from insfetch.post.content.comment import Comment

from insfetch.utils.autorrefering_attributes import AutorefferingAttributes
from insfetch.utils.funcs import get_proxies, cc_get

@AutorefferingAttributes
class PostHandler:
    __attributes__ = ['articleBody', 'commentCount', 'contentLocation',
                      'dateCreated', 'dateModified', 'headline']

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

    def _match_interaction(self, interaction):
        parsed_type = interaction['interactionType'].split('/')[-1]
        count = interaction['userInteractionCount']

        match parsed_type:
            case 'CommentAction': return {'comments': count}
            case 'LikeAction': return {'likes': count}
            case 'WatchAction': return {'views': count}
            case _: return {'unmapped': count}

    def identifier(self):
        return cc_get(self._post_dict, ['identifier', 'value'])

    def interaction_statistic(self):
        interactions = [self._match_interaction(i)
                        for i in cc_get(self._post_dict, ['interactionStatistic'])]

        return {k: v for i in interactions for k, v in i.items()}

    def author(self):
        return [Author(a, __ref__=a) for a in self._post_dict.get('author')]

    def comment(self):
        return [Comment(c, __ref__=c) for c in self._post_dict.get('comment')]

    @property
    def image(self):
        return [Image(__ref__=i) for i in self._post_dict.get('image')]

    def video(self):
        return [Video(__ref__=v) for v in self._post_dict.get('video')]
