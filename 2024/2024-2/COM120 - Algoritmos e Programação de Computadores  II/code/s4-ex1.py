class Pilha():
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)
        
    def top(self):
        if len(self.data) > 0:
            return self.data[-1]
        
    def empty(self):
        return not len(self.data) > 0
    

p = Pilha()
p.push(4)
p.push(5)
p.push(6)


while not p.empty():
    print(p.pop())
    
    if p.empty():
        print(p.empty())


## Para visualizar os dados no VSCode, precisa do print()