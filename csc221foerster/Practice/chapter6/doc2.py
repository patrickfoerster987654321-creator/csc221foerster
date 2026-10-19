"""
  >>> 4 in d
  True
  >>> 'name' in d
  False
  >>> d['name'] = 'Eric'
  >>> 'name' in d
  True
"""
d = {4: 'thing'}

if __name__ == '__main__':
    import doctest
    doctest.testmod()
