'''Access packaged resources.

Works also with zipapp. See: 
https://stackoverflow.com/a/67493286/272735
https://docs.python.org/3.10/library/zipapp.html
https://docs.python.org/3.10/library/importlib.html#module-importlib.resources
'''
from importlib.resources import read_text

def read(resource:str) -> str:
    return read_text(__package__, resource)