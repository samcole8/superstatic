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