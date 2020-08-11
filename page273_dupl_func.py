def outter():
    a = 1

    def inner1():
        b = 2

        def inner2():
            c = 3
            print(a,b,c)

        inner2()

    inner1()

outter()