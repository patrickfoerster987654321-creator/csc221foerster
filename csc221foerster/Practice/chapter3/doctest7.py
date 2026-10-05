"""
  >>> a_list[3]
  42
  >>> a_list[6]
  'Ni!'
  >>> len(a_list)
  8
"""
a_list = [0,1,2,42,4,5,'Ni!',7]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
