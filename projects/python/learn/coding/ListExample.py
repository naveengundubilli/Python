bikes = ['trek', 'redline', 'giant', 'activa']

for bike in bikes:
    print(bike)

bikes.append('ding')
bikes.append('dong')

print(bikes)
# Numerical list example

squares = []

for x in range(1, 11):
    squares.append(x ** 2)

print(squares)

bikes2 = bikes.copy()

print(bikes2)
