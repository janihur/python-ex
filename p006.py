#
# Only def creates a new scope
#

def foo():
    print(a) # prints ok
    print(b) # raises NameError

def main():
    b = 2 # def creates a scope so this is local
    foo()

if __name__ == '__main__':
    a = 1 # no scope so this is global
    main()
