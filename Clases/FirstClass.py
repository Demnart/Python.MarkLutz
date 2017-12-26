class FirstClass:

    def setvalue(self,value):
        self.data = value


    def display(self):
        print(self.data)

class SecondClass(FirstClass):
        def display(self):
            print('Current value = "%s"' % self.data)

def main():
    x = FirstClass()
    y = FirstClass()
    z = SecondClass()
    z.setvalue("Юху это ООП")
    x.setvalue(1)
    y.setvalue("hello")
    x.display()
    y.display()
    z.display()


if __name__ == '__main__':
    main()
