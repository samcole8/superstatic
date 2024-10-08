from flask import Flask

superstatic = Flask(__name__)


@superstatic.route("/")
@superstatic.route("/<path:url_path>")
def serve(url_path=""):
    return 404


superstatic.run()
