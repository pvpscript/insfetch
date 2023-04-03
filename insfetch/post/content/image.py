class Image:
    def __init__(self, image_data):
        self._image_data = image_data

    def quantity(self):
        return len(self._image_data)

    def dimensions(self, index):
        width = self._image_data[index]['width']
        height = self._image_data[index]['height']

        return f'{width}x{height}'

    def url(self, index):
        return self._image_data[index]['url']

    def caption(self):
        return self._image_data['caption']
