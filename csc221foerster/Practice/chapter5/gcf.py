def gcf(m, n):
    """
      >>> gcf(10, 25)
      5
      >>> gcf(8, 12)
      4
      >>> gcf(5, 12)
      1
      >>> gcf(24, 12)
      12
    """
    while n:
        m,n = n, m % n
    return m

if __name__ == '__main__':
    import doctest
    doctest.testmod()
