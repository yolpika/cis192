""" Homework 1
-- Due Sunday, September 11th at 23:59
-- Before starting, read
https://www.cis.upenn.edu/~cis192/homework/
-- Always write the final code yourself
-- Cite any websites you referenced
-- Use the PEP-8 checker for full style points:
https://pypi.python.org/pypi/pep8
"""
import math


def fizzbuzz(n):
    """ If n is divisible by 3, return "Fizz"
    If n is divisible by 5, return "Buzz"
    If n is divisible by 3 and 5, return "FizzBuzz"
    Else, do nothing.
    """
    if n % (3 * 5) == 0:
        return 'FizzBuzz'

    if n % 5 == 0:
        return 'Buzz'

    if n % 3 == 0:
        return 'Fizz'


def snapcrackle(n):
    """ If n is an int, return "Snap"
    If n is a float, return "Crackle"
    Else, do nothing.
    """
    if type(n) == int:
        return 'Snap'


def is_prime(n):
    """ Return True if n is prime and False otherwise.
    Use this function to help write 'nth_prime' below.
    """

    if n <= 1:
        return False

    """
    Sieve of Eratosthenes
    """
    clist = [i for i in range(2, n + 1)]
    plist = []

    while clist[0] <= math.sqrt(n):
        plist.append(clist[0])
        for m in clist:
            if m % plist[-1] == 0:
                clist.remove(m)

    plist.extend(clist)
    return n in plist


def nth_prime(n):
    """ Return the nth prime number.
    """
    if n < 1:
        return None

    count = 0
    i = 2
    while True:
        if is_prime(i):
            count += 1
            if count == n:
                break
        i += 1
    return i


def gcd_iter(n, m):
    """ An iterative function that calculates the GCD of n and m.
    Note that there is a function from the fractions module,
    fractions.gcd(a, b), that computes this -- do not use this
    function, but replicate its behavior exactly (including for
    negative or 0 inputs). See its documentation here:
    https://docs.python.org/3/library/fractions.html
    """
    gcds = []
    for d in range(2, min(abs(n), abs(m)) + 1):
        if (n % d == 0) and (m % d == 0):
            gcds.append(d)

    sign = 1
    if n < 0 or m < 0:
        sign = -1

    if len(gcds):
        return sign * max(gcds)

    return 1


def gcd_rec(n, m):
    """ A recursive function that calculates the GCD of n and m.
    """

    """ Euclidean Algorithm.
    """
    r = n % m
    if r == 0:
        return m
    else:
        gcd = gcd_rec(m, r)
    return gcd


def fib_iter(n):
    """ An iterative function that calculates the nth Fibonacci number.
    By convention, we'll say that the 1st Fibonacci number is 0
    and the 2nd Fibonacci number is 1.
    """
    x = [0, 1]
    for i in range(2, n):
        x.append(x[i - 1] + x[i - 2])

    f = x[n - 1]

    return f


def fib_rec(n):
    """ A recursive function that calculates the nth Fibonacci number.
    """
    if n == 1:
        return 0
    if n < 2:
        return 1

    return fib_rec(n - 1) + fib_rec(n - 2)


def main():
    pass


if __name__ == "__main__":
    """ Runs main() if we run this file with 'python3 hw1.py'. """
    main()
