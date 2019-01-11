"""Define a new function with default arguments using mutable and inmutable"""
def f(a, inmutable="Hola ", mutable=[], castMutableOnInmutable=None):
    inmutable + a
    mutable.append(a)
    if castMutableOnInmutable is None:
        castMutableOnInmutable = []
    castMutableOnInmutable.append(a)
    print(inmutable)
    print(mutable)
    print(castMutableOnInmutable)

f("Hola")
f("Mundo")
f("Cruel")