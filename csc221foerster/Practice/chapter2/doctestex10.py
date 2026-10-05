"""
  >>> type(this)
  <class 'str'>
  >>> type(that)
  <class 'int'>
  >>> type(something)
  <class 'float'>
"""

this = "2"
that = 2
something = 2.3

if __name__ == '__main__':
    import doctest
    doctest.testmod()
