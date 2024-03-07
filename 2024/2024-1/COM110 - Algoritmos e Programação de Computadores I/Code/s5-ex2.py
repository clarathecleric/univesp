print('Será que é um triângulo?')

a = eval(input('Digite o valor de A: '))
b = eval(input('Digite o valor de B: '))
c = eval(input('Digite o valor de C: '))

maiorLado = max(a,b,c)

## Eu uso parênteses para visualizar melhor, mas dá pra fazer sem

if (a + b + c - maiorLado > maiorLado) and ((a == b != c) or (b == c != a) or (c == a != b)):
    print('É um triângulo isósceles.')

elif (a + b + c - maiorLado > maiorLado) and (a != b != c):
    print('É um triângulo escaleno.')

elif (a + b + c - maiorLado > maiorLado) and (a == b == c):
    print('É um triângulo equilátero.')

else:
    print('Não é um triângulo.')