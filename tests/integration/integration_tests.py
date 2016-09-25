# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import os

from pycrc import py_to_crc
from tests import test


join = os.path.sep.join


class IntegrationTestCase(test.CrcTestCase):

    def test_module_and_classes(self):
        python_file = 'flask_ctx'
        result = py_to_crc(join([
            self.test_files,
            python_file
        ]))

        module, classes = result['module'], result['classes']
        cls_1, cls_2 = classes[1:]

        self.assertEqual(cls_1['name'], 'AppContext')
        self.assertEqual(cls_1['colaborators'], ['app'])
        self.assertEqual('The application context binds an application object implicitly\n'
                         'to the current thread or greenlet, similar to how the\n'
                         ':class:`RequestContext` binds request information.  The application\n'
                         'context is also implicitly created if a request context is created\n'
                         'but the application is not on top of the individual application\ncontext.',
                         cls_1['responsability'])

        self.assertEqual(cls_2['name'], 'RequestContext')
        self.assertIn('The request context contains all request relevant information.', cls_2['responsability'])
        self.assertEqual(cls_2['colaborators'], ['app', 'environ', 'request'])

        self.assertEqual(module['name'], 'flask_ctx')
        self.assertEqual(module['colaborators'], ['sys',
                                                  'update_wrapper',
                                                  'HTTPException',
                                                  '_request_ctx_stack',
                                                  '_app_ctx_stack',
                                                  'appcontext_pushed',
                                                  'appcontext_popped',
                                                  'BROKEN_PYPY_CTXMGR_EXIT',
                                                  'reraise'])
        self.assertEqual('flask.ctx\n~~~~~~~~~\n\nImplements the objects'
                         ' required to keep the context.'
                         '\n\n:copyright: (c) 2015 by Armin Ronacher.\n'
                         ':license: BSD, see LICENSE for more details.', module['responsability'])
