import requests
from requests import Response

from sucre import HttpCaller


def setup_response(
    mocker,
    request_mock_method,
    response,
    status_code=200,
    status_side_effect=[],
    text="",
):
    response_mock = mocker.MagicMock(spec=Response)
    if isinstance(response, list):
        response_mock.json.side_effect = response
    else:
        response_mock.json.return_value = response
    if isinstance(status_code, list):
        type(response_mock).status_code = mocker.PropertyMock(side_effect=status_code)
    else:
        type(response_mock).status_code = mocker.PropertyMock(return_value=status_code)
    type(response_mock).text = mocker.PropertyMock(return_value=text)
    request_mock_method.return_value = response_mock
    return response_mock


def test_request(mocker):
    url = "http://some_url.com"
    get_mock = mocker.patch("requests.get")
    setup_response(mocker, get_mock, {})
    caller = HttpCaller(url, requests.get)

    caller.call()

    get_mock.assert_called_once_with(url)


def test_request_with_kwargs(mocker):
    url = "http://some_url.com"
    get_mock = mocker.patch("requests.get")
    setup_response(mocker, get_mock, {})
    caller = HttpCaller(url, requests.get)

    caller.call(headers={}, auth={})

    get_mock.assert_called_once_with(url, headers={}, auth={})


def test_we_get_a_valid_response(mocker):
    url = "http://some_url.com"
    get_mock = mocker.patch("requests.get")
    response_mock = setup_response(mocker, get_mock, {})
    stub = mocker.stub(name="successful call")
    caller = HttpCaller(url, requests.get)
    caller.success_handler = stub

    caller.call(headers={}, auth={})

    get_mock.assert_called_once_with(url, headers={}, auth={})
    stub.assert_called_once_with(response_mock)
