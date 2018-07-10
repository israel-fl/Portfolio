from flask import render_template, current_app as app, Blueprint

blueprint = Blueprint('home', __name__)


@blueprint.route("/")
def landing():
    return render_template("index.html")


@blueprint.route("/sitemap", methods=["GET"])
def sitemap():
    return render_template("sitemap.xml")


# Administration
@blueprint.route("/health", methods=["GET"])
def health():
    return '', 200
