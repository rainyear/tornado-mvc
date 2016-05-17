from __future__ import absolute_import
from . import BaseController

class HomeHandler(BaseController):
    def get(self):
        self.write('Hello tornado-mvc!')
