import requests
from requests import Response

from sucre import HttpCaller


def test_request(mocker):
    url = "http://some_url.com"
    get_mock = mocker.patch("requests.get")
    get_mock.return_value = {}
    caller = HttpCaller(url, requests.get)
    caller.call()
    get_mock.assert_called_once_with(url)


def test_request_with_kwargs(mocker):
    url = "http://some_url.com"
    get_mock = mocker.patch("requests.get")
    get_mock.return_value = {}
    caller = HttpCaller(url, requests.get)
    caller.call(headers={}, auth={})
    get_mock.assert_called_once_with(url, headers={}, auth={})


def test_we_get_a_response(mocker):
    url = "http://some_url.com"
    get_mock = mocker.patch("requests.get")
    response_mock = mocker.MagicMock(spec=Response)
    get_mock.return_value = response_mock
    caller = HttpCaller(url, requests.get)
    actual_response = caller.call(headers={}, auth={})
    get_mock.assert_called_once_with(url, headers={}, auth={})
    assert isinstance(actual_response, Response)
