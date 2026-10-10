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
    stri = ""
    for letter in s:
        if letter == old:
            stri += new
        else:
            stri += letter

    return stri.join(stri.split(stri))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
