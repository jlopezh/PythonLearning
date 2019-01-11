a, b = 0, 1
fibo = []
while a < 100:
    fibo.append(a)
    a, b = b, a+b

print(fibo)
