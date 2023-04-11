from api.httpbin_api import http_bin_api
from http import HTTPStatus


def test_time_out():
    res = http_bin_api.time_out(4)

    assert res.status_code == HTTPStatus.OK
