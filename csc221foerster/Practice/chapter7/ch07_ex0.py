class Foo:
    """
      >>> foo = Foo(42, 'eggs')
      >>> foo.age
      42
      >>> foo.food
      'eggs'
      >>> foo.message()
      'I am 42 and I love eggs!'
    """
    def __init__(self, age, food):
        self.age = age
        self.food = food

    def message(self):
        return f'I am {self.age} and I love {self.food}!'





if __name__ == '__main__':
    import doctest
    doctest.testmod()
