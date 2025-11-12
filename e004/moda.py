# moda is primitive module that should be transparent to users of modb

from enum import Enum, unique

@unique
class ValueType(Enum):
    FOO = 0
    BAR = 1

def get_primitive_value() -> ValueType:
    return ValueType.FOO