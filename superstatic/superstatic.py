from flask import Flask
import argparse

superstatic = Flask(__name__)


@superstatic.route("/")
@superstatic.route("/<path:url_path>")
def serve(url_path=""):
    return 404


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
