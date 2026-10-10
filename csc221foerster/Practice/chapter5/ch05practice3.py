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
        


if __name__ == '__main__':
    import doctest
    doctest.testmod()
