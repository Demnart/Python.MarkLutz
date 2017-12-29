"""__getitem__- Операция получения значения по индексу и среза.
В данном модуле и классе мы узнаем как можно использовать перегрузку
оператора получения индекса и среза"""

class Indexer:
    data = [1,2,3,4,5]

    def __getitem__(self, item):
        print('Getitem =>', item)
        return self.data[item]

if __name__ == "__main__":
    x = Indexer()
    print(x[1])
    print(x[2:4])
    print(x[::2])