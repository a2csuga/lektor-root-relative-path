# -*- coding: utf-8 -*-

try:
    # py3
    from urllib.parse import urljoin, quote
except ImportError:
    # py2
    from urlparse import urljoin
    from urllib import quote

from lektor.pluginsystem import Plugin
from furl import furl


class RootRelativePathPlugin(Plugin):
    name = u'root-relative-path'
    description = u'Returns root relative path list as tuple like \
[(toppage_url, toppage_name), ...(parent_url, parent_name), (url, name)]'

    def on_setup_env(self, **extra):
        navi_top_page_name = self.get_config().get('navi_top_page_name') or 'Top Page'
        def root_relative_path_list(current_url):
            url = '/'
            name = navi_top_page_name
            path_list = [(url, name)]

            # furl('/blog').path.segments retunrs ['/blog']
            # But furl('/').path.segments retunrs ['']
            # insted []. So return value here before in to the loop
            if current_url == '/':
                return path_list

            for i in furl(current_url).path.segments:
                url = quote(urljoin(url, '%s' % i))
                name = i
                path_list.append((url, name))
                url = url + '/'

            return path_list
        self.env.jinja_env.filters['root_relative_path_list'] = root_relative_path_list
