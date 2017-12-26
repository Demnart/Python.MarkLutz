import item

class SecondClass(item.FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)


if __name__ == '__main__':
    x = item.FirstClass()
    x.setvalue("hello")
    x.display()
    y = SecondClass()
    y.setvalue(1)
    y.display()

