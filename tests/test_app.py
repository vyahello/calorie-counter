import pytest
from counter import application
from flask.testing import Client


def __is_code(app: Client, route: str, code: str) -> bool:
    return code in app.get(route)[1]


def __is_success(app: Client, route: str) -> bool:
    return __is_code(app, route, code='200')


@pytest.fixture(scope='module')
def app() -> Client:
    return Client(application)


@pytest.mark.parametrize('route', ('/', '/index', '/home'))
def test_route(app: Client, route: str) -> None:
    assert __is_success(app, route)
