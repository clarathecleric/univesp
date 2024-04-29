class Lista():
    def __init__(self):
        self.data = []

    def insert(self, x):
        self.data.append(x)

    def remove(self):
        if len(self.data) > 0:
            return self.data.pop(0)

    def top(self):
        if len(self.data) > 0:
            return self.data[0]

    def empty(self):
        return not len(self.data) > 0
    

l = Lista()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)


while not l.empty():
    if not l.empty():
        l.remove()
        print(l.top())
    
    if l.empty():
        print(l.empty())


## Para visualizar os dados no VSCode, precisa do print()