# Note: Some examples with list, set, dictionaries and tuples.

# import module sys to get the type of exception
import sys

# first example
numbers = range(1, 10)
odd = []

print('Numbers: ', numbers)
print('\n')

for number in numbers:
    if number % 2 == 0:
        odd.append(number)

print('Odd numbers: ', odd)


# second example
print('\n')
someList = [1, 2, 3, 3, 3, 4]  # Note: list is mutable.
print('someList: ', someList)
print('someList[3]: ', someList[3])
print('someList.__len__(): ', someList.__len__())

print('\n')
someSet = set()
someSet.update({1, 2, 3, 3, 3, 4})  # Note: set.
print('someSet: ', someSet)
print('someSet.__iter__().__next__(): ', someSet.__iter__().__next__())
print('someSet.__len__(): ', someSet.__len__())

print('\n')
someTuple = ('chriniko', 'soft eng', 26)  # Note: tuple is immutable.
print('someTuple: ', someTuple)
print('someTuple[0]: ', someTuple[0])

print('\n')
popularWebFrameworks = {  # Note: dictionary.
    'Java' : ['Spring', 'JavaEE', 'Dropwizard', 'Play'],
    'Python' : ['Django', 'Flusk']
}
try:
    print(popularWebFrameworks['e'])
except KeyError:
    print('Key does not exist!', sys.exc_info()[0], "occurred.")
print(popularWebFrameworks['Java'][1])



