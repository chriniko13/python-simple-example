# Note: some examples with classes, inheritance, polymorphism, monkey patching.


# intro to classes
class Person(object):
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def fullname(self):
        return "%s %s" % (self.first, self.last)

    def __str__(self):
        return "Person: " + self.fullname()


p1 = Person('niko', 'chri')

print(p1.fullname())

print(p1.__str__())

print(p1)

print(Person.__str__(p1))

print(p1.first)
p1.first = 'yolo'
print(p1.first)

print(type(p1))


# inheritance
class SuperHero(Person):
    def __init__(self, first, last, nick):
        super(SuperHero, self).__init__(first, last)
        self.nick = nick

    def __getattr__(self, item):
        # This special method is called when normal attribute lookup fails
        # In Python, mocks are
        # trivial to implement using __getattr__ and __setattr__
        if item is 'my_dyn_method':
            return lambda x: "%s-%s" % (x.first, x.last)
        else:
            raise AttributeError(item)

    def nick_name(self):
        return "I am %s" % self.nick


s1 = SuperHero('first', 'last', 'nick')
print(s1)

print(s1.nick_name())

print(s1.fullname())

print(SuperHero.nick_name(s1))

print(type(s1))

print(type(s1) is SuperHero)

print(type(type(s1)))

print(isinstance(s1, SuperHero))
print(isinstance(s1, Person))
print(issubclass(s1.__class__, Person))


# getting dynamic (monkey patching, __attr__ method, etc.)
def foo(self):
    print('\nthis is not good power!\n')


Person.foo = foo
print(s1.foo())

try:
    del s1.foo
    print(s1.foo())
except AttributeError:
    print('you have deleted it...\n')

print(s1.my_dyn_method , '\n')
print(s1.my_dyn_method() , '\n')



# classic polymorphism
# In short, use inheritance for shared behavior, not for polymorphism.
class Square(object):
    def draw(self, canvas):
        print('square canvas:', canvas)


class Circle(object):
    def draw(self, canvas):
        print('circle canvas:', canvas)


shapes = [Square(), Circle()]
for shape in shapes:
    shape.draw('some canva here')
