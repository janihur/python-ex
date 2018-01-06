from pathlib import Path

def g():
    print('module {0}: function f()'.format(Path(__file__).stem))
