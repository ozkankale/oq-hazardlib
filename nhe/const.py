"""
Module :mod:`nhe.const` defines various constants.
"""


class ConstantContainer(object):
    """
    Class that doesn't support instantiation.

    >>> ConstantContainer()
    Traceback (most recent call last):
        ...
    AssertionError: do not create objects ConstantContainer, \
use class properties instead
    """
    def __init__(self):
        raise AssertionError('do not create objects %s, '
                             'use class properties instead'
                             % type(self).__name__)


class TRT(ConstantContainer):
    """
    Container for constants that define Tectonic Region Types.
    """
    # Constant values correspond to the NRML schema definition.
    ACTIVE_SHALLOW_CRUST = 'Active Shallow Crust'
    STABLE_CONTINENTAL = 'Stable Shallow Crust'
    SUBDUCTION_INTERFACE = 'Subduction Interface'
    SUBDUCTION_INTRASLAB = 'Subduction IntraSlab'
    VOLCANIC = 'Volcanic'

    ALL = set((ACTIVE_SHALLOW_CRUST, STABLE_CONTINENTAL,
               SUBDUCTION_INTERFACE, SUBDUCTION_INTRASLAB,
               VOLCANIC))

    @classmethod
    def is_valid(cls, value):
        """
        Return ``True`` if ``value`` references a correct tectonic region type.

        >>> TRT.is_valid('Active Shallow Crust')
        True
        >>> TRT.is_valid('Active Shallo Crust')
        False
        """
        return value in cls.ALL