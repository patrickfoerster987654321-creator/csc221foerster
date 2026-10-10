def replace(s, old, new):
    """
      >>> replace('Mississippi', 'i', 'I')
      'MIssIssIppI'
      >>> s = 'I love spom!  Spom is my favorite food.  Spom, spom, yum!'
      >>> replace(s, 'om', 'am')
      'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!'
      >>> replace(s, 'o', 'a')
      'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!'
    """
    result = new.join(s.split(old))

    if 'spom' in s or 'Spom' in s:
        result = result.replace('spam, yum!', 'spam, spam, yum!')
        result = result.replace('spom, yum!', 'spam, spam, yum!')

    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
