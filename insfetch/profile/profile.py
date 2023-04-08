from .content.related_profile import RelatedProfile
from .content.timeline_media import TimelineMedia

from insfetch.utils.autoreffering_attributes import AutorefferingAttributes

from insfetch.utils.funcs import cc_get

@AutorefferingAttributes
class Profile:
    __attributes__ = ['biography', 'fbid', 'full_name', 'has_clips',
                      'has_guides', 'has_channel', 'id', 'is_business_account',
                      'is_professional_account', 'is_supervised_user',
                      'is_joined_recently', 'guardian_id',
                      'business_contact_method', 'business_email',
                      'business_email', 'business_phone_number',
                      'business_category_name', 'category_name',
                      'is_private', 'is_verified', 'profile_pic_url',
                      'profile_pic_url_hd', 'connected_fb_page', 'pronouns']

    def __init__(self, data):
        self._data = data

    def bio_links(self):
        b_links = self._data.get('bio_links')

        if b_links is None:
            return ''

        if (links := b_links[0].get('url')) is not None:
            for l in b_links[1:]:
                links += '\n' + l.get('url')

        return links

    def bio_entities(self):
        b_entities = cc_get(dict_data=self._data,
                            chain=['biography_with_entities', 'entities'])

        if b_entities is None or len(b_entities) == 0:
            return ''

        if (entities := cc_get(b_entities[0], ['user', 'username'])) is not None:
            for e in b_entities[1:]:
                entities += '\n' + cc_get(e, ['user', 'username'])

        return entities

    def num_followers(self):
        return cc_get(self._data, ['edge_followed_by', 'count'])

    def num_follows(self):
        return cc_get(self._data, ['edge_follow', 'count'])
    

    def related_profiles(self):
        if not hasattr(self, '_related_profiles'):
            rp_data = cc_get(dict_data=self._data,
                             chain=['edge_related_profiles', 'edges'])

            self._related_profiles = (
                None
                if rp_data is None
                else [RelatedProfile(__ref__=rp.get('node')) for rp in rp_data]
            )

        return self._related_profiles

    def timeline_media(self):
        if not hasattr(self, '_timeline_media'):
            tm_data = cc_get(dict_data=self._data,
                             chain=['edge_owner_to_timeline_media', 'edges'])

            self._timeline_media = (
                None
                if tm_data is None
                else [TimelineMedia(tm['node'], __ref__=tm.get('node'))
                      for tm in tm_data]
            )

        return self._timeline_media
