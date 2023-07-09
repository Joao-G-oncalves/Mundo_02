n = int(input('Digite um número para saber se ele é primo: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print(f'\033[33m', end='')
        tot +=1
    else:
        print(f'\033[31m',end='')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {n} foi divisível {tot} vezes')
if tot == 2:
    print(f'e por isso, o número {n} é PRIMO!')
else:
    print(f'e por isso, o número {n} não é PRIMO!')
