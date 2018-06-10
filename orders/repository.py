# Note: protocols example

def sayHello():
    print('hello there\n')


class OrderRepository(object):

    def __init__(self, cargo):
        self.cargo = cargo

    #protocols
    def __contains__(self, key):
        return 1 if key in self.cargo else 0

    def __getitem__(self, item):
        for var in self.cargo:
            if var == item:
                return var

        return None

    def __setitem__(self, key, value):
        for var in self.cargo:
            if var == key:
                self.cargo.remove(var)
                self.cargo.append(value)
                return value

        return None


repo = OrderRepository(['order %s' % i for i in range(1, 10)])


