from flask import Flask
from dotenv import load_dotenv
import markdown
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()
ROOT = os.environ.get("SS_ROOT")

def insert_markdown(html, path):
    md_file = path + "/" + path.split("/")[-1] + ".md"
    with open(md_file, "r") as file:
        md = file.read()
    return html.replace("<!--markdown-->", markdown.markdown(md))

def construct(target, path):
    """Construct HTML for provided target."""
    with open(target, "r") as file:
        html = file.read()
    if "<!--markdown-->" in html:
        html = insert_markdown(html, path)
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

def convert(path):
    """Convert directory path to HTML file location."""
    html_file = path.split("/")[-1] + ".html"
    return path + "/" + html_file

@app.route('/')
@app.route('/<path:subpath>')
def serve(subpath="", root=ROOT):
    """Serve an HTTP request."""
    path = os.path.normpath(root + "/" + subpath)
    target = convert(path)
    if os.path.isfile(target):
        response = template(construct(target, path), path, root)
    else:
        response = "Not Found", 404
    return response