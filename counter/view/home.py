from flask.blueprints import Blueprint
from flask import Response, render_template

blueprint: Blueprint = Blueprint(__name__, __name__)


@blueprint.route("/")
@blueprint.route("/index")
@blueprint.route("/home")
def index() -> str:
    """Returns home page route."""
    return render_template("index.html")


@blueprint.errorhandler(404)
def not_found() -> Response:
    """Returns page not found."""
    return Response("The page was not found", status=404)
