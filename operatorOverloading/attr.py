class SomeAttr:
    def __getattr__(self, item):
        if item == "age":
            return 40
        else:
            raise AttributeError

if __name__ == "__main__":
    x = SomeAttr()
    print(x.age)
    print(x.name)