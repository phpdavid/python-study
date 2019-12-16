def f1():
    a = 10
    b = 30

    def f2():
        a = 20
        print(a)
    print(b)
    f2()
    print(a)


f1()
