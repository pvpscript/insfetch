from insfetch.utils.autoreffering_attributes import AutorefferingAttributes

@AutorefferingAttributes
class Comment:
    __attributes__ = ['text', 'dateCreated']

    def __init__(self, data):
        self._data = data

    def author(self):
        return [Author(a, __ref__=a for a in self._data.get('author')]
