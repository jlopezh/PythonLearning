a = set('abcde')
b = set('aeiou')

print(a | b)
print(a & b)

print(a - b)
print(a ^ b)

print({x for x in 'abra cadabra' if x not in 'abc'})
print({x for x in 'este si esta' if x in 'es'})