from insfetch.utils.autorrefering_attributes import AutorefferingAttributes

@AutorefferingAttributes
class Image:
    __attributes__ = ['caption', 'representativeOfPage', 'height', 'width',
                      'url']
