from pathlib import Path

def f():
    print('module {0}: function f()'.format(Path(__file__).stem))
