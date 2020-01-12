import pytest
from counter import Bind


@pytest.fixture(scope="module")
def bind() -> Bind:
    return Bind("0.0.0.0:5001")


def test_host(bind: Bind) -> None:
    assert bind.host == "0.0.0.0"


def test_port(bind: Bind) -> None:
    assert bind.port == 5001
