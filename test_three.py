# Note: some more examples-plays with lists. Also list comprehensions, generator expressions and lambdas.

import math
import sys

numbers = range(5)
factorials = []

# classic way
for num in numbers:
    factorials.append(math.factorial(num))

print(factorials)

# functional way
factorial2 = list(map(math.factorial, range(5)))
print(factorial2)

example = list(map(lambda x: x ** 2, range(4)))
print(example)

# list comprehensions (iterable)
someList = [math.factorial(item) for item in range(5)]
print(someList)
print('sizeof someList:', sys.getsizeof(someList))

# generator expressions (iterator protocol)
print('\n')
someBigList = (math.factorial(item) for item in range(10) if item % 2 != 0)
print('sizeof someBigList:', sys.getsizeof(someBigList))
for x in someBigList:
    print(x, '\n')

# filter example
print('\n')
result = list(filter(lambda x: x >= 0, range(-10, 10)))
print(result)

print('\n')
a = [1, 2, 3, 5, 7, 9]
b = [2, 3, 5, 6, 7, 8]
print(list(filter(lambda x: x in a, b)))

result = list(map(pow, [2, 3, 4], [10, 11, 12]))
print(result)

# reduce example
from functools import reduce

print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))
