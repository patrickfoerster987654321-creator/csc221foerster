from point import Point
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
    def __init__ (self, data):
        self.data = data

    def nums(self):
        n = []
        for thing in self.data:
            if type(thing) == int or type(thing) == float:
                n.append(thing)


        return n

    def seqs(self):
         s = []
         for thing in self.data:
             if type(thing) == str or type(thing) == tuple or type(thing) == list:
                 s.append(thing)
         return s
     
    def others(self):
        o = []
        for thing in self.data:
            if type(thing) == bool:
                o.append(thing)
        return o
def distance(p1, p2):
    """
      >>> p1 = Point(1, 2)
      >>> p2 = Point(4, 6)
      >>> distance(p1, p2)
      5.0
      >>> p3 = Point(16, 11)
      >>> distance(p2, p3)
      13.0
    """
    dy = p2.y - p1.y
    dx = p2.x - p1.x
    return ((dx ** 2) + (dy ** 2)) ** 0.5
class NumberSet:
    """
      >>> nums = NumberSet([2, 4, 6])
      >>> print(nums)
      [2, 4, 6]
      >>> nums.mean()
      4.0
      >>> nums.median()
      4
      >>> nums.mode()
      [2, 4, 6]
      >>> nums2 = NumberSet([1, 2, 6, 6])
      >>> nums2.mean()
      3.75
      >>> nums2.median()
      4.0
      >>> nums2.mode()
      [6]
      >>> numset = [3, 5, 19, 42, 5, 42, 11]
      >>> nums3 = NumberSet(numset)
      >>> nums3.numlist
      [3, 5, 5, 11, 19, 42, 42]
      >>> numset
      [3, 5, 19, 42, 5, 42, 11]
      >>> round(nums3.mean())
      18
      >>> nums3.median()
      11
      >>> nums3.mode()
      [5, 42]
    """
    def __init__(self, data):
        self.numlist = sorted(data)

    def __str__(self):
        return f"{self.numlist}"

    def mean(self):
        count = 0
        s = 0
        for num in self.numlist:
            s += num
            count += 1
        return s / count

    def median(self):
        mid = len(self.numlist) // 2
        if len(self.numlist) % 2 != 0:
            return self.numlist[mid]
        else:
            return (self.numlist[mid - 1] + self.numlist[mid]) / 2

    def mode(self):
        counts = {}
        for num in self.numlist:
            counts[num] = counts.get(num, 0) + 1

        max_count = max(counts.values())
        return [num for num, count in counts.items() if count == max_count]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
