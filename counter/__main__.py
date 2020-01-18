from typing import NamedTuple, Any
import click
from counter import Bind, easyrun


class _Arguments(NamedTuple):
    """Returns human-readable list of user's arguments."""

    bind: Bind
    debug: bool


def _arguments(*args: Any) -> _Arguments:
    """Returns list of user's arguments."""
    return _Arguments(*args)


@click.command()
@click.option(
    "--bind", "-b", default="0.0.0.0:5001", show_default=True, help="Socket address to launch app on e.g '0.0.0.0:5001'"
)
@click.option("--debug", "-d", default=False, show_default=True, is_flag=True, help="Enable or disable debug option")
def _count_calorie_app(bind: str, debug: bool) -> None:
    """The program allows to manipulate with calorie counter app."""
    arguments = _arguments(Bind(bind), debug)
    easyrun(bind=arguments.bind, debug=arguments.debug)


if __name__ == "__main__":
    _count_calorie_app()
