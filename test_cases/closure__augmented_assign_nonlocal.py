# augmented assignment with nonlocal variable
def outer():
    x = 10

    def inner():
        nonlocal x
        x += 5

    inner()
    return x


outer()
# Return=15
