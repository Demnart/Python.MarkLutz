class FirstClass:

    def setvalue(self,value):
        self.data = value


    def display(self):
        print(self.data)

def main():
    x = FirstClass()
    y = FirstClass()
    x.setvalue(1)
    y.setvalue("hello")
    x.display()
    y.display()



if __name__ == '__main__':
    main()
