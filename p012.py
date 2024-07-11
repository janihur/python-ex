# context manager
# https://docs.python.org/3/glossary.html#term-context-manager
# https://realpython.com/python-with-statement/

class ContextManager1:
    def __enter__(self):
        print("--- entering the context 1")
        # Initialization code here
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("-- exiting the context 1")
        # Cleanup code here

from contextlib import contextmanager

@contextmanager
def ContextManager2(name):
    print(f'--- entering the context "{name}"')
    try:
        yield
    finally:
        print(f'-- exiting the context "{name}"')

with ContextManager1() as manager1:
    print("  inside the context 1")
    context2_name = 'FOO'
    with ContextManager2(context2_name):
        print(f'    inside the context {context2_name} in context 1')
        print(f'    raising exception in context {context2_name}')
        raise Exception(f'exception in context {context2_name}')