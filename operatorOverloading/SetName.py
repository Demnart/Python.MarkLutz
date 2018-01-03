"""Динамическая установка атрибута"""


class Set:
    def __setattr__(self, key, value):
        if key == "age":
            self.__dict__[key] = value
        else:
            raise AttributeError


if __name__ == "__main__":
    x = Set()
    x.age = 50
    print(x.age)

