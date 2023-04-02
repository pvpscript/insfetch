from html.parser import HTMLParser

class PostPageParser(HTMLParser):
    _data = None
    _flag_found_data = False
    _flag_disable = False

    def _match_attrs(self, attrs):
        return [a[0] == 'type' and a[1] == 'application/ld+json'
                for a in attrs]

    def _reset(self):
        self._data = None
        self._flag_found_data = False
        self._flag_disable = False

    def feed(self, *args, **kwargs):
        self._reset()
        super().feed(*args, **kwargs)

    def handle_starttag(self, tag, attrs):
        if (self._flag_found_data == False and
                tag == 'script' and self._match_attrs(attrs)):
            self._flag_found_data = True

    def handle_data(self, data):
        if self._flag_found_data and self._flag_disable == False:
            self._data = data
            self._flag_disable = True

    @property
    def data(self):
        return self._data
