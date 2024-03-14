## Pedir para o usuário digitar um número inteiro positivo. Caso contrário, emitir uma mensagem e pedir novamente.

num = eval(input('Digite um número inteiro positivo: '))

while num < 0:
    num = eval(input('Digite um número inteiro positivo: '))
print('Fim')