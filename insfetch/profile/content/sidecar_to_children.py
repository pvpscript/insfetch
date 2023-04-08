from insfetch.utils.autoreffering_attributes import AutorefferingAttributes

from insfetch.utils.funcs import cc_get

@AutorefferingAttributes
class SidecarToChildren:
    __attributes__ = ['id', 'shortcode', 'dimensions', 'display_url',
                      'fact_check_overall_rating', 'fact_check_information',
                      'gating_info', 'sharing_friction_info',
                      'media_overlay_info', 'media_preview', 'owner',
                      'is_video', 'has_upcoming_event', 'accessibility_caption']

    def __init__(self, data):
        self._data = data

    @property
    def tagged_users(self):
        if not hasattr(self, '_tagged_users'):
            tu_data = cc_get(dict_data=self._data,
                             chain=['edge_media_to_tagged_user', 'edges'])

            self._tagged_users = (
                None
                if tu_data is None
                else [TaggedUser(__ref__=cc_get(t_user, ['node', 'user']))
                      for t_user in tu_data]
            )

        return self._tagged_users
