# Inner function reads outer variable via closure
def outer():
    x = 10

    def inner():
        return x  # reads x from outer scope

    return inner()


outer()
# Return=10
