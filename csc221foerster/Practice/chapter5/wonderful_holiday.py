def wond_hol(startday, daysgone):
    """
    >>> wond_hol(3, 137)
    'Sunday'
    >>> wond_hol(2, 39)
    'Saturday'
    >>> wond_hol(1, 3)
    'Thursday'
    """
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    daysgone = daysgone % 7
    date = (startday + daysgone) % 7
    return days[date]
