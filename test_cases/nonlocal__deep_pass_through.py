# Deep pass-through: variable captured through 4 levels
# Each level must declare nonlocal to pass the cell through
def level0():
    val = 1

    def level1():
        nonlocal val
        val = val + 1

        def level2():
            nonlocal val
            val = val + 10

            def level3():
                nonlocal val
                val = val + 100
                return val

            return level3()

        return level2()

    result = level1()  # val: 1 -> 2 -> 12 -> 112
    return (result, val)


level0()
# Return=(112, 112)
