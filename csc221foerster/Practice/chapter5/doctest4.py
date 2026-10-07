def is_even(n):
    """
    >>> is_even(6)
    True
    >>> is_even(9)
    False
    >>> is_even(495969540947327823832987)
    False
    """
    if n % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
