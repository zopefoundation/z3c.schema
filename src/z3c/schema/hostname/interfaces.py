##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
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

"""
__docformat__ = "reStructuredText"

import zope.schema
import zope.schema.interfaces

from z3c.schema.i18n import MessageFactory as _


class IHostName(zope.schema.interfaces.IURI,
                zope.schema.interfaces.IFromUnicode):
    """Host name field."""


class InvalidHostName(zope.schema.ValidationError):
    __doc__ = _("""The specified host name is not valid.""")
