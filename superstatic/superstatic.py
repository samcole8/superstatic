from flask import Flask, abort
import os

app = Flask(__name__)

ROOT = "index"

def sanitise(path):
    """Check user-input path is within ROOT."""
    normalised_path = os.path.normpath(path)
    abspath = os.path.abspath(normalised_path)
    absroot = os.path.abspath(ROOT)
    if os.path.commonpath([abspath, absroot]) != absroot:
        raise ValueError("Path is outside the allowed ROOT directory.")
    else:
        return os.path.normpath(path)

def convert(path):
    """Convert directory path to HTML file location."""
    html_file = path.split("/")[-1] + ".html"
    return path + "/" + html_file

def construct(target):
    """Construct HTML for provided target."""
    with open(target, "r") as file:
        html = file.read()
    return html

@app.route('/')
@app.route('/<path:path>')
def serve(path=""):
    """Serve an HTTP request."""
    # Sanitise request
    try:
        request = sanitise(ROOT + "/" + path)
    except ValueError as e:
        print(e)
        abort(400)
    # Get target HTML file for request
    target = convert(request)
    # Return 404 if not found
    if not os.path.isfile(target):
        abort(404)
    else:
        return construct(target)