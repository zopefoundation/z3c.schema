###############################################################################
#
# Copyright 2006 by refline (Schweiz) AG, CH-5630 Muri
#
###############################################################################
"""Special Fields

$Id$
"""
__docformat__ = "reStructuredText"
import zope.interface
import zope.schema
from zope.schema.interfaces import IField, ValidationError

from z3c.schema.optchoice import interfaces


class OptionalChoice(zope.schema.Choice):
    """Optional Choice field."""

    zope.interface.implements(interfaces.IOptionalChoice)

    def __init__(self, value_type, **kw):
        super(OptionalChoice, self).__init__(**kw)
        # whine if value_type is not a field
        if value_type is not None and not IField.providedBy(value_type):
            raise ValueError("'value_type' must be field instance.")
        self.value_type = value_type

    def _validate(self, value):
        try:
            super(OptionalChoice, self)._validate(value)
        except ValidationError:
            self.value_type._validate(value)

    def fromUnicode(self, value):
        try:
            return super(OptionalChoice, self).fromUnicode(value)
        except ValidationError:
            return self.value_type.fromUnicode(value)
