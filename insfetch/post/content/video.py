from insfetch.utils.autoreffering_attributes import AutorefferingAttributes

@AutorefferingAttributes
class Video:
    __attributes__ = ['uploadDate', 'description', 'name', 'caption', 'height',
                      'width', 'contentUrl', 'thumbnailUrl']
