from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()
ROOT = os.environ.get("SS_ROOT")

def convert(path):
    """Convert directory path to HTML file location."""
    html_file = path.split("/")[-1] + ".html"
    return path + "/" + html_file

def construct(target):
    """Construct HTML for provided target."""
    with open(target, "r") as file:
        html = file.read()
    return html

def template(html, path, root):

    def traverser(start, end):
        current = start
        while current != end:
            yield current
            current = os.path.dirname(current)
        yield end

    for directory in traverser(path, root):
        template = directory + "/template.html"
        if os.path.isfile(template):
            with open(template, "r") as file:
                template_html = file.read()
            return template_html.replace('<!--template-->', html)
    return html

@app.route('/')
@app.route('/<path:subpath>')
def serve(subpath="", root=ROOT):
    """Serve an HTTP request."""
    path = os.path.normpath(root + "/" + subpath)
    target = convert(path)
    if os.path.isfile(target):
        response = construct(target)
    else:
        response = "Not Found", 404
    return response