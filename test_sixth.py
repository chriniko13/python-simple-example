# Note: simulating main

def some():
    print('some')

def someOther():
    print('someOther')


def main(args):
    some()
    someOther()
    print(args)


print(__name__)  # Note: let's see the current namespace.


if __name__ == "__main__":
    import sys
    main(sys.argv)

