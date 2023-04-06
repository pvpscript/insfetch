from insfetch.utils.autorrefering_attributes import AutorefferingAttributes

@AutorefferingAttributes
class SidecarForChildren:
    __attributes__ = ['id', 'shortcode', 'dimensions', 'display_url',
                      'fact_check_overall_rating', 'fact_check_information',
                      'gating_info', 'sharing_friction_info',
                      'media_overlay_info', 'media_preview', 'owner',
                      'is_video', 'has_upcoming_event', 'accessibility_caption']

    def __init__(self, data):
        self._data = data

    def tagged_users(self):
        if not hasattr(self, '_tagged_users'):
            tu_data = self._data['edge_media_to_tagged_user']['edges']
            self._tagged_users =  [TaggedUser(__ref__=t_user['node']['user'])
                                   for t_user in tu_data]

        return self._tagged_users
