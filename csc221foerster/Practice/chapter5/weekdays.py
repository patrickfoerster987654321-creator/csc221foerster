def week_days(numday):
    """
    >>> week_days(6)
    'Saturday'
    >>> week_days(3)
    'Wednesday'
    >>> week_days(1)
    'Monday'
    """
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return days[numday]



if __name__ == '__main__':
    import doctest
    doctest.testmod()
