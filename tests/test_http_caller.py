import requests

from sucre import HttpCaller


def test_request(mocker):
    url = "http://some_url.com"
    get_mock = mocker.patch("requests.get")
    get_mock.return_value = {}
    caller = HttpCaller(url, requests.get)
    caller.call()
    get_mock.assert_called_once_with(url)
