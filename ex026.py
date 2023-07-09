print('-=-' * 5)
print('GERADOR DE PA!')
print('-=-' * 5)
a1 = int(input('Qual o primeiro termo: '))
r = int(input('Qual a razão da PA: '))
cont = 1
while cont <= 10:
    print(f'{a1} ► ', end='')
    a1 += r
    cont += 1
print('Final!')
