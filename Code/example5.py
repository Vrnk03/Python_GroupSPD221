name = "Tomas"


# def say_hello():
#     print(globals())
#     print(locals())
#     print(f"Hello {name}")
#
# say_hello()


def say_hello():
    name1 = "Bob"
    global name
    name = "Bob"
    print(globals())
    print(locals())
    print(f"Hello {name}")


# say_hello()


n = 40


def outer():
    # global n
    n = 6

    def inner():
        nonlocal n
        n = 15
        print("inner: ", n)

        def inner_inner():
            nonlocal n
            n = 20
            print("inner_inner: ", n)

        inner_inner()
        print("inner: ", n)

    inner()
    print("outer: ", n)

outer()