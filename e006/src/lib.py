'''
A dummy function module used by application module.
'''

from time import sleep

def is_foo(x: str) -> bool:
    # simulate processing delay and provide a visual hint when running tests
    sleep(3)
    return impl_(x) == 'FOO'

def is_bar(x: str) -> bool:
    return impl_(x) == 'BAR'

def impl_(x: str) -> str:
    return x.strip().upper()