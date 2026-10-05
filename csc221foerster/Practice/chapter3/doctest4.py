"""
  >>> whatsthis[2]
  42
  >>> type(whatsthis[4])
  <class 'list'>
  >>> whatsthis[6:8]
  [11, 'what is this?']
  >>> len(whatsthis)
  10
"""

whatsthis=[0,1,42,3,[0,1],5,11,'what is this?',8,9]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
