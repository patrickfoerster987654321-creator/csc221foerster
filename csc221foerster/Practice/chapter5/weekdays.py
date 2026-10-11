def week_days(numday):
    """
    >>> numday(6)
    Saturday
    >>> numday(3)
    Wednesday
    >>> numday(1)
    Monday
    """
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return days[numday]



if __name__ == '__main__':
    import doctest
    doctest.testmod()
