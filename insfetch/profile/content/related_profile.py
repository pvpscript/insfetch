from insfetch.utils.autoreffering_attributes import AutorefferingAttributes

@AutorefferingAttributes
class RelatedProfile:
    __attributes__ = ['id', 'full_name', 'is_private', 'is_verified',
                      'profile_pic_url', 'username']
