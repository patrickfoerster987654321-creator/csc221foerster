import math

def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(4)
    False
    >>> is_prime(37)
    True
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
                   return False
        return True



if __name__ == '__main__':
    import doctest
    doctest.testmod()
