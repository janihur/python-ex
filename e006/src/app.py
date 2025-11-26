'''
A dummy application module that uses lib module functions.
'''

# pay attention what is the name you should mock as the import style matters
# https://nedbatchelder.com/blog/201908/why_your_mock_doesnt_work.html
# when imported this way you have to mock app.is_foo and app.is_bar
# NO lib.is_foo or lib.is_bar
from lib import is_foo, is_bar

def run(foo: str, bar: str) -> str:
    return f"(foo {is_foo(foo)})(bar {is_bar(bar)})"