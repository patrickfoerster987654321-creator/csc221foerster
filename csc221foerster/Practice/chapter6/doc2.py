"""
  >>> 4 in d
  True
  >>> 'name' in d
  False
  >>> d['name'] = 'Eric'
  >>> 'name' in d
  True
"""
d = {'num':4}

if __name__ == '__main__':
    import doctest
    doctest.testmod()
