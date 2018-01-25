#
# Find out a variable type and get a key value from dict with default value if
# key not available.
#

def f():
    return 'this is a string'

def g():
    return {'a': 1, 'b': 'str' }

def main():
    x = f()
    print(type(x))
    if type(x) is str:
        print("it's a string!")
        print(f'(x = {x})')

    x = g()
    print(type(x))
    if type(x) is dict:
        print("it's a dict!")
        # use default value if key doesn't exists in a dictionary
        print(f"(x.a = {x.get('a', 0)})")
        print(f"(x.b = {x.get('b', 'null')})")
        print(f"(x.c = {x.get('c', 'default value')})")

if __name__ == '__main__':
    main()
