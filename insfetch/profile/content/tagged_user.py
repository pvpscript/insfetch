from insfetch.utils.autorrefering_attributes import AutorefferingAttributes

@AutorefferingAttributes
class TaggedUser:
    __attributes__ = ['full_name', 'id', 'is_verified', 'profile_pic_url',
                      'username']
