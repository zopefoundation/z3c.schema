##############################################################################
#
# Copyright (c) 2008 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""
$Id:$
"""
__docformat__ = "reStructuredText"

import unittest
from zope.schema.interfaces import RequiredMissing
from zope.schema.tests.test_field import FieldTestBase
from zope.testing import doctest
from zope.testing.doctestunit import DocFileSuite

from z3c.schema.baseurl import BaseURL
from z3c.schema.baseurl import InvalidBaseURL


class BaseURLTest(FieldTestBase):

    _Field_Factory = BaseURL
    _convert = str

    def testValidate(self):
        field = self._Field_Factory(title=u'BaseURL field', description=u'',
            readonly=False, required=False)
        field.validate(None)
        field.validate(self._convert('host:123.123.123.123/'))
        field.validate(self._convert('host:123/'))
        field.validate(self._convert('http://www.host.com:123/'))
        field.validate(self._convert('http://123.123.123.123:123/'))

    def testValidateRequired(self):
        field = self._Field_Factory(title=u'BaseURL field', description=u'',
            readonly=False, required=True)
        self.assertRaises(RequiredMissing, field.validate, None)

    def testBadStringType(self):
        field = self._Field_Factory(title=u'BaseURL field')
        self.assertRaises(InvalidBaseURL, field.validate, u'123.123')

    def test_newlines(self):
        field = self._Field_Factory(title=u'BaseURL field')
        self.assertRaises(InvalidBaseURL, field.validate,
            self._convert('host\nfoo'))


def test_suite():
    return unittest.TestSuite((
        DocFileSuite('README.txt',
            optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS,),
        unittest.makeSuite(BaseURLTest),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')