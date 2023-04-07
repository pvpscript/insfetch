from insfetch.utils.autoreffering_attributes import AutorefferingAttributes

from insfetch.utils.funcs import cc_get

@AutorefferingAttributes
class Author:
    __attributes__ = ['image', 'name', 'alternateName', 'url']

    def __init__(self, data):
        self._data = data

    def identifier(self):
        return cc_get(self._data, ['identifier', 'value'])
