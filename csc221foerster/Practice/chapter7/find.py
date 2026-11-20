def find(str, ch, start=0, end=None):
    """
        >>> find("apple", "p")
        1
        >>> find("apple", "p", 2)
        2
        >>> find("apple", "p", 3)
        -1

    """
    if end is None:
        end = len(str)
    index = start
    while index < end:
        if str[index] == ch:
            return index
        index = index + 1
    return -1
