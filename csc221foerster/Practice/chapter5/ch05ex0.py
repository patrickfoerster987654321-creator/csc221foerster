def count_digits(digit, n):
    """
      >>> count_digits(5, 1055030250)
      3
      >>> count_digits(9, 909)
      2
      >>> count_digits(7, 7777)
      4
      >>> count_digits(7, 1234)
      0
    """
    d = 0
    count = 0
    while n > 0:
        d = n % 10
        if d == digit:
            count += 1
        n //=10

    print(count)



def find_average(numbers):
    """
      >>> find_average([5, 10])
      7.5
      >>> find_average([5, 10, 15])
      10.0
      >>> find_average((1, 2, 2, 3))
      2.0
      >>> find_average([19])
      19.0
    """
    s = 0
    for num in numbers:
        s += num
    avg = s/len(numbers)
    return avg


def only_evens(nums):
    """
      >>> only_evens([3, 8, 5, 4, 12, 7, 2])
      [8, 4, 12, 2]
      >>> my_nums = [4, 7, 19, 22, 42]
      >>> only_evens(my_nums)
      [4, 22, 42]
      >>> my_nums
      [4, 7, 19, 22, 42]
    """
    en = []
    for num in nums:
        if num % 2 == 0:
            en.append(num)
        
    return en


def keep_only_evens(nums):
    """
      >>> some_nums = [3, 8, 5, 4, 12, 7, 2]
      >>> keep_only_evens(some_nums)
      >>> some_nums
      [8, 4, 12, 2]
    """
    nums[:] = [num for num in nums if num % 2 == 0]



def g(x):
    """
    >>> g(3)
    20
    >>> g(-1)
    -8
    >>> g(4)
    57
    """
    return x ** 3 - 7

def h(x):
    """
    >>> h(-2)
    19
    >>> h(0)
    5
    >>> h(3)
    14
    """
    return (2*(x**2))-(3*x)+5

def k(x):
    """
    >>> k(5)
    2149
    >>> k(2)
    -29
    >>> k(3)
    37
    """
    return (x**5)-(8 * (x**3))+(7*x)-11



def find_median(l):
    """
    >>> find_median([2,1,4,6])
    3.0
    >>> find_median([5,2,6])
    5.0
    """
    lst = list(l)
    n = len(lst)
    
    if n == 0:
        return None

    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    if n % 2 == 1:
        return float(lst[n // 2])
    else:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2.0




def find_mode(l):
    """
    >>> find_mode([1,4,6,9])
    5.0
    >>> find_mode([4,6,0,9])
    4.75
    >>> find_mode([1,2,3])
    2.0
    """
    sum = 0
    for num in l:
        sum += num
    return float(sum/len(l))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
