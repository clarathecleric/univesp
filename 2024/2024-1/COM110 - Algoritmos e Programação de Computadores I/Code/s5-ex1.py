altura = eval(input('Digite sua altura:'))
sexo = input('Digite h para homem ou m para mulheres:')

if sexo == 'h':
    peso = (7.2*altura)-58
else:
    peso = (62.1*altura)-44.7
   
print('Seu peso ideal é:', peso)
