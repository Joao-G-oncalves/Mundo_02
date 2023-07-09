num = int(input('Digite um número para saber se ele é primo: '))
tot = 0
for cont in range(1, num+1):
    if num % cont == 0:
        print('\033[1:31m', end=' ')
        tot = tot + 1
    else:
        print('\033[1:34m', end=' ')
    print(cont, end='')
print(f'\n\033[mO número {num} foi dividido {tot} vezes,')

if tot > 2:
    print('e por isso, ele não é primo!')
else:
    print('e por isso, ele é primo!')
