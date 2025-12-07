# Closure that uses both nonlocal and global
g = 1000


def make_closure():
    x = 1

    def closure():
        global g
        nonlocal x
        result = g + x
        g = g + 1
        x = x + 10
        return result

    return closure


c = make_closure()
r1 = c()  # g=1000, x=1 -> returns 1001, then g=1001, x=11
r2 = c()  # g=1001, x=11 -> returns 1012, then g=1002, x=21
r3 = c()  # g=1002, x=21 -> returns 1023, then g=1003, x=31
(r1, r2, r3, g)
# Return=(1001, 1012, 1023, 1003)
