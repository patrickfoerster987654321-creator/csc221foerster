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

class Bar:
    """
      >>> bar = Bar()
      >>> bar.this
      'Ni!'
      >>> bar.that
      'shrubbery'
      >>> bar.speak(2)
      'Ni! Ni!'
      >>> bar.speak(5)
      'Ni! Ni! Ni! Ni! Ni!'
    """
    def __init__(self, this='Ni!', that='shrubbery'):
        self.this = this
        self.that = that

    def speak(self, num):
        count = 1
        s = ''
        while count <= num:
            s += self.this + ' '
            count += 1
        return s.strip()

class Seqtools:
    """
      >>> myseq = Seqtools([1, 2, 'a', 7, ('x', 'y'), 'yup', 11.3, True])
      >>> myseq.data
      [1, 2, 'a', 7, ('x', 'y'), 'yup', 11.3, True]
      >>> myseq.nums()
      [1, 2, 7, 11.3]
      >>> myseq.seqs()
      ['a', ('x', 'y'), 'yup']
      >>> myseq.others()
      [True]
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
