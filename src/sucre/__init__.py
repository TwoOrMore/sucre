class HttpCaller:
    """Wrapper around requests to setup the call as a data structure with
    callbacks
    """

    def __init__(self, url, method):
        self._url = url
        self._method = method
        self._success_handler = self._default_success_handler
        self._error_handler_4xx = self._default_error_handler_4xx
        self._error_handler_5xx = self._default_error_handler_5xx

    def _default_success_handler(self, response):
        return response

    def _default_error_handler_4xx(self, response):
        return response

    def _default_error_handler_5xx(self, response):
        return response

    def call(self, **kwargs):
        response = self._method(self._url, **kwargs)

        if response.status_code == 500:
            self._error_handler_5xx(response)

        if response.status_code == 400:
            self._error_handler_4xx(response)

        if response.status_code == 200:
            self._success_handler(response)

    @property
    def success_handler(self):
        return self._success_handler

    @success_handler.setter
    def success_handler(self, callback):
        self._success_handler = callback

    @property
    def error_handler_4xx(self):
        return self._error_handler_4xx

    @success_handler.setter
    def error_handler_4xx(self, callback):
        self._error_handler_4xx = callback

    @property
    def error_handler_5xx(self):
        return self._error_handler_5xx

    @success_handler.setter
    def error_handler_5xx(self, callback):
        self._error_handler_5xx = callback
