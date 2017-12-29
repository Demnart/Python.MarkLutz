class Indexer:
    def __getitem__(self, item): # Метод __getitem__ перехватывает обращение экземляра в формате x[i]
        return item ** 2

if __name__ == "__main__":
    x  = Indexer()
    print(x[6])