# Note: some examples with functions, nested functions.

# functions
def some_func():
    return nested_func


def nested_func(s):
    return s


print(some_func()(5))

print('\n')


def say_hello(name, *args, **kwargs):
    print(name, '\n')
    print(args[0], '\n')
    print(kwargs['exp'], '\n')


say_hello('hello', 1, 2, 3, prof="soft eng", exp="JVM Engineer")

# functions and tuples
print('\n')


def multi_return():
    return 10, 20, ['a', 'b']  # automatic tuple packing


result = multi_return()
print(result)
var1, var2, var3 = multi_return()  # automatic tuple unpacking
print(var3)

print('\n')


def ternary(a, b, c):
    print(a, b, c)


ternary(1, 2, 3)
ternary(*(1, 2, 3))
ternary(**{'a': 1, 'b': 2, 'c': 3})


# functions inside functions
def make_function(parity):
    if parity == 'even':
        filter = lambda num: num % 2 == 0
    elif parity == 'odd':
        filter = lambda num: num % 2 != 0
    else:
        raise AttributeError("Unknown parity: " + parity)

    def inner(numbers):
        return [num for num in numbers if filter(num)]

    return inner


print(make_function('even')(range(10)))
print(make_function('odd')(range(10)))
try:
    print(make_function('some')(range(10)))
except AttributeError:
    print('ooops')
