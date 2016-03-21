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

## How to use

Insert the following line in the template (e.g. layout.html) which you would like to show navigation.

```
{% for i in this._path | root_relative_path_list %}
  >><a href="{{i[0]}}">{{i[1]}}</a>
{% endfor %}
```

Then, navigation is shown as below in case the page 'blog/first-post/'

```
>>Top Page >>blog >>first-post
```

If you do not want to show current page in the navigation, modify template as below.

```
{% for i in this._path | root_relative_path_list %}
  {% if not loop.last %}
    >><a href="{{i[0]}}">{{i[1]}}</a>
  {% endif %}
{% endfor %}
```
Then, navigation is shown as below.

```
>>Top Page >>blog
```

