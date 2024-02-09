# Como fazer os objetos das suas classes se tornarem iteráveis!

class Contagem:
    def __init__(self, max_number: int):
        self.max_number = max_number    

    def __iter__(self):
        self.iterator = -1
        return self

    def __next__(self):
        self.iterator += 1
        if self.iterator > self.max_number:
            raise StopIteration
        return self.iterator
    

c = Contagem(10)
for x in c:
    print(x)

for x in c:
    print(x)

