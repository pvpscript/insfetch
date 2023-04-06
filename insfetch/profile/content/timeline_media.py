from insfetch.utils.filtered_params import FilteredParams
from insfetch.utils.funcs import chained_get

from .tagged_user import TaggedUser
from .sidecar_for_children import SidecarForChildren

@FilteredParams
class TimelineMedia:
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

    def __init__(self, data):
        self._data = data

    def tagged_users(self):
        if not hasattr(self, '_tagged_users'):
            tu_data = self._data['edge_media_to_tagged_user']['edges']
            self._tagged_users =  [TaggedUser(__ref_ =t_user['node']['user'])
                                   for t_user in tu_data]

        return self._tagged_users

    def media_to_caption(self):
        if not hasattr(self, '_media_captions'):
            c_data = self._data['edge_media_to_caption']['edges']
            self._media_captions = [c['node']['text'] for c in c_data]

        return self._media_captions

    def comment_count(self):
        return self._data['edge_media_to_comment']['count']

    def like_count(self):
        return self._data['edge_media_liked_by']['count']

    def media_preview_like_count(self):
        return self._data['edge_media_preview_like']['count']

    def sidecar_to_children(self):
        if not hasattr(self, '_sidecar_for_children'):
            s_data = cc_get(dict_data=self._data,
                            chain=['edge_sidecar_to_children', 'edges'])

            self._sidecar_for_children = (
                None
                if s_data is None
                else [SidecarForChilren(__ref__=sfc['node']) for sfc in s_data]
            )

        return self._sidecar_for_children
