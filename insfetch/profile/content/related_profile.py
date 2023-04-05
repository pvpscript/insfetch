from insfetch.utils.filtered_params import FilteredParams

@FilteredParams
class RelatedProfile:
    __keys__ = ['id', 'full_name', 'is_private', 'is_verified',
                'profile_pic_url', 'username']
