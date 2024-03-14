## Armazenar nomes de pessoas em uma lista enquanto o usuário digitar strings diferentes de vazio.

l = list()
nome = input('Digite um nome: ')

while nome != '':
    l.append(nome)
    nome = input('Digite um nome: ')
print(l)

