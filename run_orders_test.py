# Note: importing and packaging example

from orders import repository as orders_repo

orders_repo.sayHello()

db = orders_repo.repo

print(db.cargo, '\n')
print('\n')


# __contains__
print('order1' in db)
print('order 1' in db)
print('\n')


# __getitem__
print(db['orderxyz'])
print(db['order 1'])
print('\n')


# __setitem__
print(db['order 1'])
db['order 1'] = 'order 1: updated'
print(db['order 1'])
print(db['order 1: updated'])
print('\n')
