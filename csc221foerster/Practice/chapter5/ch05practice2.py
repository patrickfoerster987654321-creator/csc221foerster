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


def num_digits(n):
    """
      >>> num_digits(12345)
      5
      >>> num_digits(0)
      1
      >>> num_digits(-12345)
      5
    """
    if n < 0:
        return num_digits(abs(n))
    elif n == 0:
        return 1
    else:
        count = 0
        while n > 0:
            n //= 10
            count += 1
        return count

def num_even_digits(n):
    """
      >>> num_even_digits(123456)
      3
      >>> num_even_digits(2468)
      4
      >>> num_even_digits(1357)
      0
      >>> num_even_digits(2)
      1
      >>> num_even_digits(20)
      2
    """
    if n < 0:
        return num_even_digits(abs(n))
    elif n == 0:
        return 1
    else:
        count = 0
        while n > 0:
            digit = n % 10
            if digit % 2 == 0:
                count += 1
            n = n // 10
        return count



def print_digits(n):
    """
      >>> print_digits(13789)
      9 8 7 3 1
      >>> print_digits(39874613)
      3 1 6 4 7 8 9 3
      >>> print_digits(213141)
      1 4 1 3 1 2
      >>> returned = print_digits(123)
      3 2 1
      >>> print(returned)
      None
    """
    if n == 0:
        print(0)
        return

    digits = []
    while n > 0:
        digits.append(str(n % 10))
        n //= 10

    print(" ".join(digits))


def sum_of_squares_of_digits(n):
    """
      >>> sum_of_squares_of_digits(1)
      1
      >>> sum_of_squares_of_digits(9)
      81
      >>> sum_of_squares_of_digits(11)
      2
      >>> sum_of_squares_of_digits(121)
      6
      >>> sum_of_squares_of_digits(987)
      194
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()
