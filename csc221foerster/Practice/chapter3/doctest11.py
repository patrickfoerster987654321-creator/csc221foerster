"""
  >>> another_thing[1]
  'happiness'
  >>> len(another_thing)
  5
  >>> 42 in another_thing
  True
  >>> type(another_thing) == type([])
  False
"""
another_thing = (42, 'happiness', 2,3,4)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
