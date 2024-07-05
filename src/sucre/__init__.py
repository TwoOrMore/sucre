class HttpCaller:
    """Wrapper around requests to setup the call as a data structure with
    callbacks
    """

    def __init__(self, url, method):
        self._url = url
        self._method = method
        self._success_handler = self._default_success_handler

    def _default_success_handler(self, response):
        return response

    def call(self, **kwargs):
        response = self._method(self._url, **kwargs)

        if response.status_code == 200:
            self._success_handler(response)

    @property
    def success_handler(self):
        return self._success_handler

    @success_handler.setter
    def success_handler(self, callback):
        self._success_handler = callback
