from flask import Flask
from dotenv import load_dotenv
import markdown
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()
ROOT = os.environ.get("SS_ROOT")

def markup(html, path):
    if "<!--markdown-->" in html:
        fetch(path, "md")
        html = html.replace("<!--markdown-->", markdown.markdown(md))
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

def fetch(path, extension="html"):
    with open(f"{path}/{path.split("/")[-1]}.{extension}", "r") as file:
        data = file.read()
    return data

@app.route('/')
@app.route('/<path:subpath>')
def serve(subpath="", root=ROOT):
    """Serve an HTTP request."""
    path = os.path.normpath(root + "/" + subpath)
    if os.path.exists(path):
        response = template(markup(fetch(path), path), path, root)
    else:
        response = "Not Found", 404
    return response