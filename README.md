# Lektor root-relative-path plugin

This plugin returns root-relative-path list from top page to current page as below.

```
[(toppage_url, toppage_name), ...(parent_url, parent_name), (url, name)]
```

## Installation
Add `lektor-root-relative-path` to your project from the command line:

```
lektor plugins add lektor-root-relative-path
```

See [the Lektor documentation for more instructions on installing plugins](https://www.getlektor.com/docs/plugins/).

## Configuration

Set these option in `configs/root-relative-path.ini`:

### `navi_top_page_name`

Optional. Name of top page inidicated in the navication. Default is 'Top Page'

```
navi_top_page_name = 'Root'
```

