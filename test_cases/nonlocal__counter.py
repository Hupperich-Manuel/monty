# Classic counter pattern - closure outlives defining scope
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment


counter = make_counter()
assert counter() == 1, 'first call'
assert counter() == 2, 'second call'
assert counter() == 3, 'third call'
counter()
# Return=4
