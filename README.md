# superstatic

Enhanced static sites.

## Deployment

### Basic layout

superstatic uses directories to establish hierarchy.

- A chosen folder (`index` by default) acts as the web root
- HTML files are served at requests to their parent folder of the same name

```
index
├── index.html
└── subdirectory-1
    ├── subdirectory-1.html
    └── subdirectory-2
        └── subdirectory-2.html
```

In the above example:

- `index.html` is served at `mysite.com`
- `subdirectory-1.html` is served at `mysite.com/subdirectory-1`
- `subdirectory-2.html` is served at `mysite.com/subdirectory-1/subdirectory-2`

### Templates

Templates allow you to define a consistent layout for your HTML content. Here's how to use them:

- **Location and Naming**: Templates must be called `template.html` and placed in the parent directory of the files they are meant to style.
- **Template Hierarchy**: Lower-level templates take priority, which means you can use different templates for different parts of your site.
- **Body Insertion**: Templates use the `<!--template-->` tag as a placeholder where the body of your HTML document will be inserted. Ensure this tag is present on its own line to define where content should appear.