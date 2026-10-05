"""
  >>> type(thing1)
  <class 'float'>
  >>> type(thing2)
  <class 'int'>
  >>> type(thing3)
  <class 'str'>
"""

thing1 = 4.5
thing2 = 4
thing3 = '4'

if __name__ == '__main__':
	import doctest
	doctest.testmod()
