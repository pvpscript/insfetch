import requests

class ProfileHandler:
    _API_URL = 'https://www.instagram.com/api/v1/users/web_profile_info/'

    def __init__(self, username):
        self._username = username

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
                              headers=self._headers)

        result_dict = result.json()
        if result_dict['status'].lower() != 'ok':
            raise Exception('Unable to fetch profile data for "{self._username}"')

        return result_dict['data']['user']

    def biography(self):
        return self._profile_data['biography']

    def bio_links(self):
        b_links = self._profile_data['bio_links']
        
        links = b_links[0]['url']
        for l in b_links[1:]:
            links += '\n' + l['url']

        return links

    def bio_entities(self):
        b_entities = self._profile_data['biography_with_entities']['entities']

        entities = b_entities[0]['user']['username']
        for e in b_entities[1:]:
            entities += '\n' + e['user']['username']

        return entities

    def num_followers(self):
        return self._profile_data['edge_followed_by']['count']

    def num_follows(self):
        return self._profile_data['edge_follow']['count']

    def facebook_id(self):
        return self._profile_data['fbid']

    def full_name(self):
        return self._profile_data['full_name']

    def has_clips(self):
        return self._profile_data['has_clips']

    def has_guides(self):
        return self._profile_data['has_guides']

    def has_channel(self):
        return self._profile_data['has_channel']

    def id(self):
        return self._profile_data['id']

    def is_business_account(self):
        return self._profile_data['is_business_account']

    def is_professional_account(self):
        return self._profile_data['is_professional_account']

    def is_supervised_user(self):
        return self._profile_data['is_supervised_user']

    def is_joined_recently(self):
        return self._profile_data['is_joined_recently']

    def guardian_id(self):
        return self._profile_data['guardian_id']

    def business_contact_method(self):
        return self._profile_data['business_contact_method']

    def business_email(self):
        return self._profile_data['business_email']

    def business_phone_number(self):
        return self._profile_data['business_phone_number']

    def business_category_name(self):
        return self._profile_data['business_category_name']

    def category_name(self):
        return self._profile_data['category_name']

    def is_private(self):
        return self._profile_data['is_private']

    def is_verified(self):
        return self._profile_data['is_verified']

    def profile_pic_url(self):
        return self._profile_data['profile_pic_url']

    def profile_pic_url_hd(self):
        return self._profile_data['profile_pic_url']

    def connected_fb_page(self):
        return self._profile_data['connected_fb_page']

    def pronouns(self):
        return self._profile_data['pronouns']

    def related_profiles(self): # needs to be broken down
        return self._profile_data['edge_related_profiles']['edges']

    def timeline_media(self): # needs to be broken down
        return self._profile_data['edge_owner_to_timeline_media']
