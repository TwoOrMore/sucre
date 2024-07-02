class HttpCaller:
    """Wrapper around requests to setup the call as a data structure with
    callbacks
    """

    def __init__(self, url, method):
        self._url = url
        self._method = method

    def call(self, **kwargs):
        self._method(self._url, **kwargs)
