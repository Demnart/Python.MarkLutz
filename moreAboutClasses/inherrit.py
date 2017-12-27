class Super:
    def print(self):
        print("IN Super class")

    def delegate(self):
        self.action()


class Sup(Super):
    pass


class Replacer(Super):
    def print(self):
        print("In replace method")


class Extender(Super):
    def print(self):
        print("In Extender Method")
        Super.print(self)
        print("ending extender method")


class Provider(Super):
    def action(self):
        print("in Provider.action")


if __name__ == "__main__":
    for klas in (Sup, Replacer, Extender):
        print("\n" + klas.__name__ + "....")
        klas().print()
    x = Provider()
    x.delegate()
