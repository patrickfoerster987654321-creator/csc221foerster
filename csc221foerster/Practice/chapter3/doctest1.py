"""
  >>> type(thing1)
  <class 'list'>
  >>> type(thing2)
  <class 'tuple'>
  >>> type(thing3)
  <class 'str'>
"""
thing1 = []
thing2 = ()
thing3 = ''

if __name__ == "__main__":
    import doctest
    doctest.testmod()
