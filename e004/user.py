from typing import Any
import modb

def kv(k:str, v:Any) -> str:
    if isinstance(v, int):
        return f'("{k}" {v})'
    else:
        return f'("{k}" "{v}")'

def print_value() -> None:
    val: modb.ValueType = modb.get_value()
    print(
        kv("module", val.__module__),
        kv("repr", repr(val)),
        kv("name", val.name),
        kv("value", val.value),
        kv("is modb.ValueType.FOO", val == modb.ValueType.FOO),
        kv("is modb.ValueType.BAR", val == modb.ValueType.BAR)
    )
