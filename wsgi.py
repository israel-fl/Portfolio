from app import create_app
from flask import render_template
import os

app = create_app()


# error handler
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(exception):
    app.logger.error(exception)
    return render_template('500.html'), 500


@app.template_filter('autoversion')
def autoversion_filter(filename):
    fullpath = os.path.join('app/', filename[1:])
    try:
        timestamp = str(os.path.getmtime(fullpath))
    except OSError:
        return filename
    newfilename = "{0}?v={1}".format(filename, timestamp)
    return newfilename


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, threaded=True)
