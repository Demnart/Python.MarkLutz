class Iters:
    def __init__(self, value):
        self.data = value

    # def __getitem__(self, item):
    #     print('%s' % item, end="")
    #     return self

    def __iter__(self):
        print("iter =>", end=" ")
        self.ix = 0
        return self

    def __next__(self):
        print("next: ", end="")
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, item):
        print("Contains: ", end="")
        return item in self.data


if __name__ == "__main__":
    X = Iters([1, 2, 3, 4, 5])
    print(3 in X)
    for i in X:
        print(i, end="  |  ")
    print()
    print([x**2 for x in X])
    print(list(map(bin,X)))
    I = iter(X)
    while True:
        try:
            print(next(I), end= "   @  ")
        except StopIteration:
            break

