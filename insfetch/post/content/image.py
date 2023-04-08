from insfetch.utils.autoreffering_attributes import AutorefferingAttributes

@AutorefferingAttributes
class Image:
    __attributes__ = ['caption', 'height', 'width', 'url']
    __dict_attributes__ = [{'representativeOfPage': 'representative_of_page'}]
                      
