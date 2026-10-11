def will_ring(timenow, hourslater):
    """
    >>> will_ring('2 p.m.', 51)
    5 p.m.
    >>> will_ring('2 p.m', 37)
    3 a.m.
    """
    timenow = timenow.replace('.', '').strip()
    hour_str, period = timenow.split()
    hour = int(hour_str)

    if period.lower() == 'pm' and hour != 12:
        hour += 12
    elif period.lower() == 'am' and hour == 12:
        hour = 0

    future_hour = (hour + hourslater) % 24

    if future_hour == 0:
        return "12 a.m."
    elif future_hour == 12:
        return "12 p.m."
    elif future_hour > 12:
        return f"{future_hour-12} p.m."
    else:
        return f"{future_hour} a.m."
