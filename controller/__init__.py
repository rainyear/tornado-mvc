from __future__ import absolute_import

import tornado.web

class BaseController(tornado.web.RequestHandler):
    def render(self, tpl, **render_data):
        if not tpl.endswith('html'):
            tpl = "{}.html".format(tpl)
        super().render(tpl, **render_data)
class My404(BaseController):
    def get(self):
        self.render('404')

from .HomeHandler import HomeHandler
__all__ = ['HomeHandler', 'My404']
