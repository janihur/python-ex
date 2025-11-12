# a module used by users and using moda internally

from enum import Enum, unique
import moda

# re-declared here so that moda remains transparent to modb users
@unique
class ValueType(Enum):
    FOO = 0
    BAR = 1

def get_value() -> ValueType:
    val: moda.ValueType = moda.get_primitive_value()
    # don't leak moda.ValueType, re-create as modb.ValueType
    return ValueType(val.value)