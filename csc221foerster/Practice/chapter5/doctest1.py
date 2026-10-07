def compare(a, b):
    """
      >>> compare(8, 4)
      1
      >>> compare(7, 7)
      0
      >>> compare(2, 9)
      -1
      >>> compare(42, 1)
      1
      >>> compare('c', 'a')
      1
      >>> compare('p', 'p')
      0
    """
    #  Your function body should begin here.
    message = ""
    if a > b:
        message = 1
    elif a < b:
        message = -1
    else:
        message = 0

    return message


if __name__ == '__main__':
    import doctest
    doctest.testmod()
