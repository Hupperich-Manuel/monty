# Cell pass-through: outer owns cell, middle passes through, inner uses it
# Tests that nonlocal declarations properly chain through multiple levels
def outer():
    x = 1

    def middle():
        nonlocal x
        x = x + 10  # x becomes 11

        def inner():
            nonlocal x
            x = x + 100  # x becomes 111
            return x

        r1 = inner()  # returns 111
        r2 = x  # x is now 111
        return r1 + r2  # 111 + 111 = 222

    return middle()


outer()
# Return=222
