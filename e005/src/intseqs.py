'''
Several integer sequence functions used to demonstrate unit testing.

Two functions use unit tests and the rest use doctests.
'''

def even(n: int) -> list[int]:
    '''
    Generate the first n even numbers.
    
    Args:
        n (int): The number of even numbers to generate.
    
    Returns:
        list: A list containing the first n even numbers.
    
    Raises:
        ValueError: If n is not a positive integer.
    
    No doctests here, see unit tests.
    '''
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    
    return [2 * i for i in range(n)]

def fibonacci1(n: int) -> list[int]:
    '''
    Generate the first n Fibonacci numbers using an iterative approach.
    
    Args:
        n (int): The number of Fibonacci numbers to generate.
    
    Returns:
        list: A list containing the first n Fibonacci numbers.
    
    Raises:
        ValueError: If n is not a positive integer.
    
    No doctests here, see unit tests.
    '''
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def fibonacci2(n: int) -> list[int]:
    '''
    Generate the first n Fibonacci numbers using a recursive approach.
    
    Args:
        n (int): The number of Fibonacci numbers to generate.
    
    Returns:
        list: A list containing the first n Fibonacci numbers.
    
    Raises:
        ValueError: If n is not a positive integer.
    
    Examples:
    >>> fibonacci2(0)
    Traceback (most recent call last):
    ...
    ValueError: n must be a positive integer.
    >>> fibonacci2(1)
    [0]
    >>> fibonacci2(2)
    [0, 1]
    >>> fibonacci2(10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    '''
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    
    def fib_recursive(k: int) -> int:
        if k == 0:
            return 0
        elif k == 1:
            return 1
        else:
            return fib_recursive(k - 1) + fib_recursive(k - 2)
    
    return [fib_recursive(i) for i in range(n)]

def odd(n: int) -> list[int]:
    '''
    Generate the first n odd numbers.
    
    Args:
        n (int): The number of odd numbers to generate.
    
    Returns:
        list: A list containing the first n odd numbers.
    
    Raises:
        ValueError: If n is not a positive integer.
    
    Examples:
    >>> odd(0)
    Traceback (most recent call last):
    ...
    ValueError: n must be a positive integer.
    >>> odd(1)
    [1]
    >>> odd(2)
    [1, 3]
    >>> odd(10)
    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    '''
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    
    return [2 * i + 1 for i in range(n)]

def primes(n: int) -> list[int]:
    '''
    Generate the first n prime numbers.
    
    Args:
        n (int): The number of prime numbers to generate.
    
    Returns:
        list: A list containing the first n prime numbers.
    
    Raises:
        ValueError: If n is not a positive integer.
    
    Examples:
    >>> primes(0)
    Traceback (most recent call last):
    ...
    ValueError: n must be a positive integer.
    >>> primes(1)
    [2]
    >>> primes(2)
    [2, 3]
    >>> primes(10)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    '''
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    seq = []
    candidate = 2
    while len(seq) < n:
        is_prime = True
        for p in seq:
            if p * p > candidate:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            seq.append(candidate)
        candidate += 1
    return seq

def recaman(n: int) -> list[int]:
    '''
    Generate the first n terms of the Recamán's sequence.
    
    Args:
        n (int): The number of terms to generate.
    
    Returns:
        list: A list containing the first n terms of the Recamán's sequence.
    
    Raises:
        ValueError: If n is not a positive integer.
    
    Examples:
    >>> recaman(0)
    Traceback (most recent call last):
    ...
    ValueError: n must be a positive integer.
    >>> recaman(1)
    [0]
    >>> recaman(2)
    [0, 1]
    >>> recaman(20)
    [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9, 24, 8, 25, 43, 62]
    '''
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    
    seq = [0]
    for i in range(1, n):
        next_val = seq[-1] - i
        if next_val > 0 and next_val not in seq:
            seq.append(next_val)
        else:
            seq.append(seq[-1] + i)
    return seq