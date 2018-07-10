from flask import Flask
import logging
from raven.contrib.flask import Sentry

sentry = Sentry()


def create_app(testing=False):
    app = Flask(__name__)

    # Setup logs to show in Gunicorns logger
    handler = logging.StreamHandler()
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)
    # fix gives access to the gunicorn error log facility
    app.logger.handlers.extend(logging.getLogger("gunicorn.error").handlers)

    # Fetch the conviguration:
    app.config.from_pyfile('../env.py')
    if app.config.get("ENVIRON") == "DEVELOPMENT":
        app.config['DEBUG'] = True
        app.config["TEMPLATES_AUTO_RELOAD"] = True

    # config file has STATIC_FOLDER='app/static'
    app.static_url_path = app.config.get('STATIC_FOLDER')

    # set the absolute path to the static folder
    app.static_folder = app.root_path + app.static_url_path

    # BLUEPRINTS
    from app.http.controllers import home
    app.register_blueprint(home.blueprint)

    # Initialize Sentry
    sentry.init_app(
        app,
        dsn=app.config.get("SENTRY_URI"),
        logging=True,
        level=logging.ERROR
    )

    return app