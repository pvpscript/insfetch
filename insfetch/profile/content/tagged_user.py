from insfetch.utils.filtered_params import FilteredParams

@FilteredParams
class TaggedUser:
    __keys__ = ['full_name', 'id', 'is_verified', 'profile_pic_url',
                'username']
