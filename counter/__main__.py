from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, _SubParsersAction
from typing import Dict, NamedTuple, Any
from counter import Bind, easyrun, application


class _Arguments(NamedTuple):
    """Returns human-readable list of user's arguments."""

    bind: Bind
    debug: bool
    command: str


def _arguments() -> _Arguments:
    """Returns list of user's arguments."""
    analytics_parser: ArgumentParser = ArgumentParser(
        description="The program allows to manipulate with calorie counter app",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    sub_parsers: _SubParsersAction = analytics_parser.add_subparsers(
        description="A list of allowed options for manipulation with calorie counter app.",
        help="It is allowed only to run calorie counter app.",
    )
    run_parser: ArgumentParser = sub_parsers.add_parser(name="run", help="Runs calorie counter app.")
    run_parser.set_defaults(command="run")
    run_parser.add_argument(
        "--bind",
        "-b",
        action="store",
        help="Socket address to launch app on e.g '0.0.0.0:5001'",
        type=str,
        default="0.0.0.0:5001",
    )
    run_parser.add_argument(
        "--debug", "-d", action="store_true", help="Enable or disable debug option", default=False,
    )
    command_line_input: Dict[str, Any] = vars(analytics_parser.parse_args())
    if not command_line_input:
        analytics_parser.print_help()
        analytics_parser.exit(1)
    command_line_input["bind"] = Bind(command_line_input["bind"])
    return _Arguments(**command_line_input)


def _run_calorie_counter_app(arguments: _Arguments) -> None:
    """Runs weather app."""
    easyrun(bind=arguments.bind, debug=arguments.debug)


if __name__ == "__main__":
    _run_calorie_counter_app(_arguments())
