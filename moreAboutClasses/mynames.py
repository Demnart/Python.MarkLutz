x = 11


def f():
    print(x)


def g():
    x = 12
    print(x)


class Names:
    x = 12

    def func(self):
        x = 33
        self.x = 55

if __name__ == "__main__":
    print(x)
    f()
    g()
    print(x)
    obj = Names()
    print(obj.x)
    print(Names.x)

    obj.func()
    print(obj.x)
    print(Names.x)
