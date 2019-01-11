"""Explain LEGB rule"""
"""Local and Global scopes"""
a_var = 'global value'

def a_func():
    a_var = 'local value'
    print(a_var, '[ a_var inside a_func() ]')

a_func()
print(a_var, '[ a_var outside a_func() ]')
print("=" * 20)


"""concept of the enclosed (E) scope. Following the order 'Local -> Enclosed -> Global'"""
a_var = 'global value'

def outer():
    a_var = 'enclosed value'

    def inner():
        a_var = 'local value'
        print(a_var)

    inner()

outer()


a_var = 'global value'

def outer():
    a_var = 'local value'
    print('outer before:', a_var)
    def inner():
        nonlocal a_var
        a_var = 'inner value'
        print('in inner():', a_var)
    inner()
    print("outer after:", a_var)
outer()
print("=" * 20)


"""LEGB - Local, Enclosed, Global, Built-in"""
a_var = 'global variable'

def len(in_var):
    print('called my len() function')
    l = 0
    for i in in_var:
        l += 1
    return l

def a_func(in_var):
    len_in_var = len(in_var)
    print('Input variable is of length', len_in_var)

a_func('Hello, World!')
print("=" * 20)


"""Scope in Loops"""
i = 1
print([i for i in range(5)])
print(i, '-> i in global')