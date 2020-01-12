from flask import Flask
from counter.builder import Bind
from counter.view import home

__all__ = ("__version__", "__author__", "easyrun", "application", "Bind")
__version__: str = "0.0.1"
__author__: str = "Volodymyr Yahello"

application: Flask = Flask(__name__)
application.register_blueprint(home.blueprint)


def easyrun(bind: Bind = Bind("0.0.0.0:5001"), debug: bool = False) -> None:
    """Runs application in standalone mode."""
    application.run(bind.host, bind.port, debug)
