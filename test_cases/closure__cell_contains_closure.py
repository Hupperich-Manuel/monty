# closure with captured cell stored in another cell - tests refcount handling
def outer():
    y = 100  # will be captured by inner, so it's a cell var

    def inner():
        return y  # inner captures y, making inner a Closure with cells

    x = inner  # x holds a Closure, and x itself is a cell var

    def get_x():
        nonlocal x
        return x  # returns the Closure from the cell

    # get the closure and call it to verify cell refcounts are correct
    f = get_x()
    return f()


outer()
# Return=100
