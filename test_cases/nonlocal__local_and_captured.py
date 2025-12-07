# Variable used both locally and captured by nested function
def outer():
    x = 1

    def inner():
        nonlocal x
        x = x + x  # double x
        return x

    # Use x locally before and after inner() modifies it
    before = x  # x = 1
    middle = inner()  # x becomes 2, returns 2
    after = x  # x = 2
    final = inner()  # x becomes 4, returns 4

    return (before, middle, after, final, x)


outer()
# Return=(1, 2, 2, 4, 4)
