# Multiple closures sharing the same cell
def make_pair():
    x = 0

    def getter():
        return x

    def setter(v):
        nonlocal x
        x = v

    return (getter, setter)


pair = make_pair()
getter = pair[0]
setter = pair[1]
assert getter() == 0, 'initial value'
setter(42)
assert getter() == 42, 'after setter'
getter()
# Return=42
