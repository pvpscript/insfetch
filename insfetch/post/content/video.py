from insfetch.utils.autoreffering_attributes import AutorefferingAttributes

@AutorefferingAttributes
class Video:
    __attributes__ = ['description', 'name', 'caption', 'height', 'width']
    __dict_attributes__ = [{'uploadDate': 'upload_date'},
                           {'contentUrl': 'content_url'},
                           {'thumbnailUrl': 'thumbnail_url'}]
