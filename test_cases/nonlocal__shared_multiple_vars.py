# Two closures that share multiple nonlocal variables
def make_ops():
    x = 0
    y = 0

    def add_to_x(n):
        nonlocal x
        x = x + n
        return x

    def add_to_y(n):
        nonlocal y
        y = y + n
        return y

    def swap():
        nonlocal x, y
        tmp = x
        x = y
        y = tmp
        return (x, y)

    def get_both():
        return (x, y)

    return (add_to_x, add_to_y, swap, get_both)


ops = make_ops()
add_x = ops[0]
add_y = ops[1]
swap = ops[2]
get = ops[3]

add_x(5)  # x=5, y=0
add_y(10)  # x=5, y=10
add_x(3)  # x=8, y=10
swap()  # x=10, y=8
get()
# Return=(10, 8)
