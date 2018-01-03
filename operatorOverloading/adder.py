class Adder:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        self.data += other


class ReprAdder(Adder):
    def __repr__(self):
        return "ReprAdder({})".format(self.data)


if __name__ == "__main__":
    y = ReprAdder(5)
    print(y)
