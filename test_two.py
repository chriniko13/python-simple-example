# Note: some more examples-plays with list.

list = list(range(1, 100))

print(list[0:5])
print(list[:5])
print(list[90:])
print(list[-1])
print(list[-5:-1])

print('\n')

numbers = [0, 1, 2, 'three', 4, 5, 6, 7, 8, 9]
print(numbers[0:9:2])
print(numbers[::2])
print(numbers[::-1])

print('\n')

copy = numbers[:]
print(copy == numbers)  # equals in java
print(copy is numbers)  # == in java
print(id(copy))  # hashCode in java
print(id(numbers))

print('\n')

numbers = [10, 20, 30]
for number in numbers:
    print(number)

for index, number in enumerate(numbers):
    print('index:', index, 'number:', number)


for num in range(len(numbers)):
    print('num:', num)

toys = ['bat', 'ball', 'truck']
if 'bat' in toys:
    print('yo bat here')

toys.append('yolo')
toys.remove('ball')
toys.sort()
print(toys)

print('\n')

stack = []
stack.append("event")
print(stack.pop())

queue = []
queue.append("event")
print(queue.pop(0))
