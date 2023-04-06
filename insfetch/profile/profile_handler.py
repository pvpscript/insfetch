import requests

from .content.related_profile import RelatedProfile
from .content.timeline_media import TimelineMedia

from insfetch.utils.autorrefering_attributes import AutorefferingAttributes

from insfetch.utils.funcs import get_proxies, cc_get

@AutorefferingAttributes
class ProfileHandler:
    __attributes__ = ['biography', 'fbid', 'full_name', 'has_clips',
                      'has_guides', 'has_channel', 'id', 'is_business_account',
                      'is_professional_account', 'is_supervised_user',
                      'is_joined_recently', 'guardian_id',
                      'business_contact_method', 'business_email',
                      'business_email', 'business_phone_number',
                      'business_category_name', 'category_name',
                      'is_private', 'is_verified', 'profile_pic_url',
                      'profile_pic_url_hd', 'connected_fb_page', 'pronouns']

    _API_URL = 'https://www.instagram.com/api/v1/users/web_profile_info/'

    def __init__(self, username):
        self._username = username

        self._proxies = get_proxies()
        self._profile_data = self._fetch()

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

    def _fetch(self):
        result = requests.get(url=self._API_URL,
                              params=self._params,
                              headers=self._headers,
                              proxies = self._proxies)

        if (result_dict := result.json())['status'].lower() != 'ok':
            raise Exception('Unable to fetch profile data for "{self._username}"')

        return cc_get(result_dict, ['data', 'user'])

    def bio_links(self):
        b_links := self._profile_data.get('bio_links')

        if b_links is None:
            return ''
        
        if (links := b_links[0].get('url')) is not None:
            for l in b_links[1:]:
                links += '\n' + l.get('url')

        return links

    def bio_entities(self):
        b_entities = cc_get(dict_data=self._profile_data,
                            chain=['biography_with_entities', 'entities'])

        if b_entities is None:
            return ''

        if (entities := cc_get(b_entities[0], ['user', 'username'])) is not None:
            for e in b_entities[1:]:
                entities += '\n' + cc_get(e, ['user', 'username'])

        return entities

    def num_followers(self):
        return cc_get(self._profile_data, ['edge_followed_by', 'count'])

    def num_follows(self):
        return cc_get(self._profile_data, ['edge_follow', 'count'])
    

    def related_profiles(self):
        if not hasattr(self, '_related_profiles'):
            rp_data = cc_get(dict_data=self._profile_data,
                             chain=['edge_related_profiles', 'edges'])

            self._related_profiles = (
                None
                if rp_data is None
                else [RelatedProfile(__ref__=rp.get('node')) for rp in rp_data]
            )

        return self._related_profiles

    def timeline_media(self):
        if not hasattr(self, '_timeline_media'):
            tm_data = cc_get(dict_data=self._profile_data,
                             chain=['edge_owner_to_timeline_media', 'edges'])

            self._timeline_media = (
                None
                if tm_data is None
                else [TimelineMedia(tm['node'], __ref__=tm.get('node'))
                      for tm in tm_data]
            )

        return self._timeline_media
