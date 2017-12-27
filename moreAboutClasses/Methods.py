"""Подробнее о методах"""

class nextClass:

    def printer(self,text):
        self.text = text
        print(self.text)


if __name__ == "__main__":
    x = nextClass()
    x.printer("hello")