def wond_hol(startday, daysgone):
    """
    >>> wond_hol(3, 137)
    'Sunday'
    >>> wond_hol(2, 39)
    'Saturday'
    >>> wond_hol(1, 3)
    'Thursday'
    """
    days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    total_days = (startday + daysgone) % 7
    return days[total_days]

if __name__ == '__main__':
    import doctest
    doctest.testmod()

