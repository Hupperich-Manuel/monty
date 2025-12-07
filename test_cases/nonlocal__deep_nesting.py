# 3 levels of nesting with nonlocal at each level
def level1():
    x = 1

    def level2():
        nonlocal x
        x = x + 10

        def level3():
            nonlocal x
            x = x + 100
            return x

        return level3()

    return level2()


level1()
# Return=111
