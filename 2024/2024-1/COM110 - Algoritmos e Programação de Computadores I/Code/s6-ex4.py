## Como calcular a soma de todos os números pares de 1 a 100?

## O acumulador deve ser definido antes do loop
ac = 0

## O valor final do range é desconsiderado, dessa forma, para atender o enunciado, precisamos manter 100 como um valor considerável.
for x in range(1,101):
    if x % 2 == 0:
        ac = ac + x
print(ac)