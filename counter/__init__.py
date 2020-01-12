from flask import Flask
from counter.builder import Bind
from counter.view import home

__all__ = ("__version__", "__author__", "easyrun")
__version__: str = "0.0.1"
__author__: str = "Volodymyr Yahello"

_application: Flask = Flask(__name__)
_application.register_blueprint(home.blueprint)


def easyrun(bind: Bind = Bind("0.0.0.0:5001"), debug: bool = False) -> None:
    """Runs application in standalone mode."""
    _application.run(bind.host, bind.port, debug)
