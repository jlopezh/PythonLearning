cars = {'Renault': 'Duster', 'Kia': 'Mohave'}

"""Using items() method"""
for k,v in cars.items():
    print(k, v)


"""Using enumerate method to get index"""
print('=' * 20)
for i, v in enumerate(cars):
    print(i, v)


"""Loop over two o more sequences"""
print('=' * 20)
car = ['Kia', 'Renault', 'BMW']
model = ['Cerato', 'Captur', "Serie A"]
hp = [101, 175, 250]
for c, m, hp in zip(car, model, hp):
    print("The power of {0} {1} is {2}hp.".format(c , m, hp))


"""Loop over a sequence in reverse"""
print('=' * 20)
for c in reversed(car):
    print(c)

"""Loop over a sequence in sorted"""
print('=' * 20)
for c in sorted(car):
    print(c)


