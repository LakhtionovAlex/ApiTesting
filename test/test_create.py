from api.questions_api import api
from http import HTTPStatus


def test_create():
    name = 'Boris'
    job = 'tester'
    res = api.create(name, job)

    assert res.status_code == HTTPStatus.CREATED
    assert res.json()['name'] == name
    assert res.json()['job'] == job

    assert api.delete_user(res.json()['id']).status_code == HTTPStatus.NO_CONTENT
