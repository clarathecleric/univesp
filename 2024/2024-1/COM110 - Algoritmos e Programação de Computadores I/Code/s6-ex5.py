## Dada uma lista de strings como segue:
## str_list = ['João', 'Roberto', 'Rafael']
## Retornar todas as vogais que ocorrem nos elementos acima.

str_list = ['João', 'Roberto', 'Rafael']

for nome in str_list:
    for c in nome:
        if c in 'aeiou':
            print(c)