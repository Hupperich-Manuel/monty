# Mixing global and nonlocal in the same function hierarchy
g = 100


def outer():
    x = 1

    def inner():
        global g
        nonlocal x
        g = g + 1
        x = x + 10
        return g + x

    return inner()


outer()
# Return=112
