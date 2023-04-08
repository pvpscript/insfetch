from insfetch.post.content.image import Image
from insfetch.post.content.video import Video
from insfetch.post.content.author import Author
from insfetch.post.content.comment import Comment

from insfetch.utils.autoreffering_attributes import AutorefferingAttributes
from insfetch.utils.funcs import cc_get

@AutorefferingAttributes
class Post:
    __attributes__ = ['headline']
    __dict_attributes__ = [{'articleBody': 'article_body'},
                           {'commentCount': 'comment_count'},
                           {'contentLocation': 'content_location'},
                           {'dateCreated': 'date_created'},
                           {'dateModified': 'date_modified'}]

    def __init__(self, data):
        self._data = data

    def _match_interaction(self, interaction):
        parsed_type = interaction['interactionType'].split('/')[-1]
        count = interaction['userInteractionCount']

        match parsed_type:
            case 'CommentAction':
                return {'comments': count}
            case 'LikeAction':
                return {'likes': count}
            case 'WatchAction':
                return {'views': count}
            case _:
                return {'unmapped': count}

    @property
    def identifier(self):
        return cc_get(self._data, ['identifier', 'value'])

    @property
    def interaction_statistic(self):
        interactions = [self._match_interaction(i)
                        for i in cc_get(self._data, ['interactionStatistic'])]

        return {k: v for i in interactions for k, v in i.items()}

    @property
    def author(self):
        if (author_dict := self._data.get('author')) is not None:
            return Author(author_dict, __ref__=author_dict)

        return None

    @property
    def comment(self):
        if (comment_dict := self._data.get('comment')) is not None:
            return Comment(comment_dict, __ref__=comment_dict)

        return None

    @property
    def images(self):
        return [Image(__ref__=i) for i in self._data.get('image')]

    @property
    def videos(self):
        return [Video(__ref__=v) for v in self._data.get('video')]
