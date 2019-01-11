fruits = ['naranja', 'banano', 'pera', 'fresa', 'mora', 'chulupa']
print(fruits)

fruits.append('zapote')
print(fruits)

fruits.extend(fruits)
print(fruits)

fruits.insert(0, 'anon')
print(fruits)

fruits.remove('pera')
print(fruits)

fruits.pop(2)
print(fruits)

print(fruits.count('zapote'))

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares_1 = [x**2 for x in range(10)]
print(squares_1)

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

print(combs)

combs_1 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combs_1)