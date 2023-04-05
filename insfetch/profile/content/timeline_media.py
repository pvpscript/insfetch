from insfetch.utils.filtered_params import FilteredParams

from .tagged_user import TaggedUser

@FilteredParams
class TimelineMedia:
    def __init__(self, data):
        self._data = data

    # EDGE_MEDIA_TO_TAGGED_USER, EDGE_MEDIA_TO_CAPTION, EDGE_MEDIA_TO_COMMENT, EDGE_LIKED_BY, EDGE_MEDIA_PREVIEW_LIKE, EDGE_SIDECAR_TO_CHILDREN

    __keys__ = ['id', 'shortcode', 'dimensions', 'display_url',
                'fact_check_overall_rating', 'fact_check_information',
                'gating_info', 'sharing_friction_info', 'media_overlay_info',
                'media_preview', 'owner', 'is_video', 'has_upcoming_event',
                'accessibility_caption', 'dash_info', 'has_audio',
                'tracking_token', 'video_url', 'video_view_count',
                'comments_disabled', 'taken_at_timestamp', 'location',
                'nft_asset_info', 'thumbnail_src', 'thumbnail_resources',
                'felix_profile_grid_crop', 'coauthor_producers',
                'pinned_for_users', 'viewer_can_reshare',
                'product_type', 'clips_music_attribution_info']

    def tagged_users(self):
        if not hasattr(self, '_tagged_users'):
            tu_data = self._data['edge_media_to_tagged_user']['edges']
            self._tagged_users =  [TaggedUser(__ref__ = t_user['node']['user'])
                                   for t_user in tu_data]

        return self._tagged_users

    def media_to_caption(self):
        pass

    def media_to_comment(self):
        pass

    def liked_by(self):
        pass

    def media_preview_like(self):
        pass

    def sidecar_to_children(self):
        pass
