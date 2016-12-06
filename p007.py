#
# Currying (function returning a function)
#

def make_adder(a):
    def f(b):
        return a + b
    return f

def make_adder2(a): return lambda b: a() + b()

def one(): return 1

def five(): return 5

def main():
    add_five = make_adder(5)
    print(add_five(1))

    add_five = make_adder2(five)
    print(add_five(one))

    add_five = make_adder2(lambda: 5)
    print(add_five(lambda: 1))

if __name__ == '__main__':
    main()
