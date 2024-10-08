from flask import Flask
import argparse
import os

superstatic = Flask(__name__)


EXTENSIONS = ["html", "md"]


def map_url(url_path):
    request = os.path.normpath((superstatic.config["WEB_ROOT"] + "/" + url_path))
    entrypoint = None
    if os.path.isfile(request):
        entrypoint = request
    elif os.path.isdir(request):
        for key in reversed(EXTENSIONS):
            test_entrypoint = request + "/index." + key
            if os.path.isfile(test_entrypoint):
                entrypoint = test_entrypoint
    return entrypoint


@superstatic.route("/")
@superstatic.route("/<path:url_path>")
def serve(url_path=""):
    entrypoint = map_url(url_path)
    return "OK"


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("web_root", type=str, help="Path to the web root directory.")
    parser.add_argument("--template", type=str, help="Template to render (optional).")

    # Parse arguments
    args = parser.parse_args()

    # Define configuration variables
    superstatic.config["TEMPLATE"] = args.template
    superstatic.config["WEB_ROOT"] = args.web_root

    # Start Flask app
    superstatic.run()
