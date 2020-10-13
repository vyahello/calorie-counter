import pytest
from counter import application
from flask.testing import Client


def __is_code(app: Client, rule: str, code: str) -> bool:
    return code in app.get(rule)[1]


def __is_success(app: Client, rule: str) -> bool:
    return __is_code(app, rule, code='200')


@pytest.fixture(scope='module')
def app() -> Client:
    return Client(application)


def test_root(app: Client) -> None:
    assert __is_success(app, rule='/')


def test_index(app: Client) -> None:
    assert __is_success(app, rule='/index')


def test_home(app: Client) -> None:
    assert __is_success(app, rule='/home')
