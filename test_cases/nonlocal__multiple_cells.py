# Multiple independent cells captured by different nested functions
def outer():
    a = 1
    b = 10
    c = 100

    def modify_a():
        nonlocal a
        a = a + 1
        return a

    def modify_b():
        nonlocal b
        b = b + 10
        return b

    def modify_c():
        nonlocal c
        c = c + 100
        return c

    def read_all():
        return a + b + c

    # Call in specific order to test cell independence
    r1 = modify_b()  # b = 20
    r2 = modify_a()  # a = 2
    r3 = modify_c()  # c = 200
    r4 = read_all()  # 2 + 20 + 200 = 222
    return (r1, r2, r3, r4)


outer()
# Return=(20, 2, 200, 222)
