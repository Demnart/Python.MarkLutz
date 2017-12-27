"""Подробнее рассматриваем Классы, переменные класса и переменные экземляра"""
class MixedVariables:
    data = 'spam' # Данная переменная является переменной класа и доступна всем экземплярам 

    def __init__(self,value):
        self.data = value

if __name__ == "__main__":
    x = MixedVariables(1)
    y = MixedVariables(3)
    print(x.data,y.data,MixedVariables.data)