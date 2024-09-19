# superstatic

Enhanced static sites.

## Guide

### Basic layout

superstatic uses directories to establish hierarchy.

- **Web Root**: A chosen folder (`index` by default) acts as the web root
- **Request Mapping**: HTML files are served at requests to their parent folder of the same name

For example:

```
index
├── index.html
└── subdirectory-1
    ├── subdirectory-1.html
    └── subdirectory-2
        └── subdirectory-2.html
```

- `mysite.com` -> `index.html`
- `mysite.com/subdirectory-1` -> `subdirectory-1.html`
- `mysite.com/subdirectory-1/subdirectory-2` -> `subdirectory-2.html`

### Templates

Templates allow you to define a consistent layout for your HTML content. Here's how to use them:

- **Location and Naming**: Templates must be called `template.html` and placed in the parent directory of the files they are meant to style.
- **HTML Insertion**: Templates use the `<!--template-->` tag as a placeholder where the body of your HTML document will be inserted.
- **Template Hierarchy**: Lower-level templates take priority, which means you can use different templates for different parts of your site.

### Markdown

Superstatic can convert Markdown (`.md` files) to HTML and embed it in your `.html` files.

- **Location & Naming**: `.md` files should follow the same convention as `.html` files, using the same name as their parent folder.
- **Markdown Insertion**: HTML generated from `.md` files is inserted at any `<!--markdown-->` tag present in the `.html` file.