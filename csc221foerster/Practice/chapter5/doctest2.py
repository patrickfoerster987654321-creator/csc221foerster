def hypotenuse(a, b):
    """
      >>> hypotenuse(3, 4)
      5.0
      >>> hypotenuse(12, 5)
      13.0
      >>> hypotenuse(7, 24)
      25.0
      >>> hypotenuse(9, 12)
      15.0
    """
    import math
    hyp = float(math.sqrt((a**2)+(b**2)), 1)
    return hyp

if __name__ == '__main__':
    import doctest
    doctest.testmod()
