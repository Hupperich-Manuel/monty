# Implicit capture - reading from enclosing scope without explicit nonlocal
def outer():
    a = 10
    b = 20

    def inner():
        # reads both a and b from outer scope
        return a + b

    return inner()


outer()
# Return=30
