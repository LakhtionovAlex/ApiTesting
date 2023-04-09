from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert


def test_register_successful():
    password = '2654dhrd'
    res = api.register_successful(password)
    res_body = res.json()

    assert res.status_code == HTTPStatus.OK
    Assert.validate_schema(res.json())

    example = {
        "id": 4,
        "token": "QpwL5tke4Pnpja7X4"
    }
    assert example == res_body


def test_register_unsuccessful():
    password = ""
    res = api.register_successful(password)
    res_body = res.json()

    assert res.status_code == HTTPStatus.BAD_REQUEST
    Assert.validate_schema(res.json())

    example = {
        "error": "Missing password"
    }
    assert example == res_body
