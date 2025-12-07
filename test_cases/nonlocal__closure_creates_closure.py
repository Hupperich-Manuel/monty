# Closure that creates another closure - nested closure factory
def outer_factory():
    outer_val = 10

    def inner_factory():
        nonlocal outer_val
        inner_val = outer_val

        def innermost():
            nonlocal inner_val
            inner_val = inner_val + 1
            return inner_val

        outer_val = outer_val + 100  # modify outer_val after capturing inner_val
        return innermost

    return inner_factory


factory = outer_factory()
closure1 = factory()  # inner_val starts at 10, outer_val becomes 110
closure2 = factory()  # inner_val starts at 110, outer_val becomes 210
r1 = closure1()  # inner_val of closure1: 10 -> 11
r2 = closure1()  # inner_val of closure1: 11 -> 12
r3 = closure2()  # inner_val of closure2: 110 -> 111
r4 = closure1()  # inner_val of closure1: 12 -> 13
(r1, r2, r3, r4)
# Return=(11, 12, 111, 13)
