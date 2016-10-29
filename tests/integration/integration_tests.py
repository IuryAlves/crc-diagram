# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import os

from pycrc import py_to_crc, project_to_crc, NotAPythonFile
from tests import test


join = os.path.join


class IntegrationTestCase(test.CrcTestCase):

    def test_file_extension_should_not_be_in_module_name(self):
        file = 'flask_ctx.py'
        result = py_to_crc(join(
            self.test_files,
            file))
        module = result['module']

        self.assertEqual(module['name'], 'flask_ctx')

    def test_raise_exception_if_is_not_python_file(self):
        file = 'not_a_python_file'

        with self.assertRaises(NotAPythonFile) as context:
            py_to_crc(join(
                self.test_files,
                file))

        self.assertIn('not_a_python_file is not a python file', str(context.exception))

    def test_project_to_crc_modules(self):
        project_folder = 'project'
        result = project_to_crc(join(
            self.test_files,
            project_folder))

        crc_0, crc_1 = list(result)

        self.assertEqual(crc_0['module']['name'], 'lib')
        self.assertEqual(crc_0['module']['responsibility'], 'A awesome lib')
        self.assertEqual(crc_0['module']['colaborators'], ['boto'])

        self.assertEqual(crc_1['module']['name'], 'main')
        self.assertEqual(crc_1['module']['responsibility'], 'The Main')
        self.assertEqual(crc_1['module']['colaborators'], ['lib'])

    def test_module_and_classes(self):
        python_file = 'flask_ctx.py'
        result = py_to_crc(join(
            self.test_files,
            python_file))

        module, classes = result['module'], result['classes']
        cls_1, cls_2 = classes[1:]

        self.assertEqual(cls_1['name'], 'AppContext')
        self.assertEqual(cls_1['colaborators'], ['app'])
        self.assertEqual('The application context binds an application object implicitly\n'
                         'to the current thread or greenlet, similar to how the\n'
                         ':class:`RequestContext` binds request information.  The application\n'
                         'context is also implicitly created if a request context is created\n'
                         'but the application is not on top of the individual application\ncontext.',
                         cls_1['responsibility'])

        self.assertEqual(cls_2['name'], 'RequestContext')
        self.assertIn('The request context contains all request relevant information.', cls_2['responsibility'])
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
                         ':license: BSD, see LICENSE for more details.', module['responsibility'])
