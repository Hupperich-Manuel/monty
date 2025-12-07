# Inner function modifies outer variable using nonlocal
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20  # modifies x in outer scope

    inner()
    return x


outer()
# Return=20
