def lots_of_letters(word):
    """
      >>> lots_of_letters('Lidia')
      'Liidddiiiiaaaaa'
      >>> lots_of_letters('Python')
      'Pyyttthhhhooooonnnnnn'
      >>> lots_of_letters('')
      ''
      >>> lots_of_letters('1')
      '1'
    """
    result = ""
    for index, letter in enumerate(word):
        result += letter * (index + 1)
    return result
        
def seperate_by_type(list_of_stuff):
    """
      >>> seperate_by_type([3, 'a', 4.2, None, (1, 2), 'b'])
      ([3, 4.2], ['a', (1, 2), 'b'], [None])
      >>> seperate_by_type([1, 3, 'xyz', 42, (0, 2), 'qwerty', [1, 0], 12])
      ([1, 3, 42, 12], ['xyz', (0, 2), 'qwerty', [1, 0]], [])
      >>> seperate_by_type([])
      ([], [], [])
    """
    numbers = []
    sequences = []
    nones = []
    bools = []

    for item in list_of_stuff:
        if item is None:
            nones.append(item)
        elif isinstance(item, (int, float)):
            numbers.append(item)
        elif isinstance(item, (str, tuple, list)):
            sequences.append(item)
        else:
            bools.append(item)
    return (numbers, sequences, nones)

def only_evens(numbers):
  """
    >>> only_evens([1, 3, 4, 6, 7, 8])
    [4, 6, 8]
    >>> only_evens([2, 4, 6, 8, 10, 11, 0])
    [2, 4, 6, 8, 10, 0]
    >>> only_evens([1, 3, 5, 7, 9, 11])
    []
    >>> only_evens([4, 0, -1, 2, 6, 7, -4])
    [4, 0, 2, 6, -4]
    >>> nums = [1, 2, 3, 4]
    >>> only_evens(nums)
    [2, 4]
    >>> nums
    [1, 2, 3, 4]
  """
  for item in numbers:
      if item % 2 == 1:
          numbers.remove(item)



  return nums


if __name__ == '__main__':
    import doctest
    doctest.testmod()
