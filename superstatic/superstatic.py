from flask import Flask, send_file
import argparse
import os
from markdown import markdown

superstatic = Flask(__name__)


def read(file_path):
    with open(file_path, "r") as file:
        file_contents = file.read()
    return file_contents


def send_html(file_path):
    html = read(file_path)
    return html


def send_md(file_path):
    md = read(file_path)
    html = markdown(md)
    return html


EXTENSION_DRIVERS = {"html": send_html, "md": send_md}


def get_extension(file_path):
    _, extension = os.path.splitext(file_path)
    return extension.lstrip(".")


def map_url(url_path):
    request = os.path.normpath((superstatic.config["WEB_ROOT"] + "/" + url_path))
    entrypoint = None
    if os.path.isfile(request):
        entrypoint = request
    elif os.path.isdir(request):
        for key in reversed(EXTENSION_DRIVERS.keys()):
            test_entrypoint = request + "/index." + key
            if os.path.isfile(test_entrypoint):
                entrypoint = test_entrypoint
    return entrypoint


@superstatic.route("/")
@superstatic.route("/<path:url_path>")
def serve(url_path=""):
    entrypoint = map_url(url_path)
    if entrypoint is None:
        # Serve 404 if entrypoint doesn't exist.
        response = "404 Not Found", 404
    else:
        # Serve entrypoint
        extension = get_extension(entrypoint)
        if extension in EXTENSION_DRIVERS:
            driver = EXTENSION_DRIVERS[extension]
        else:
            driver = send_file
        response = driver(entrypoint), 200
    return response


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
