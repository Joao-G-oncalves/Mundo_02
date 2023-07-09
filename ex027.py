print('-=-' * 5)
print('GERADOR DE PA!')
print('-=-' * 5)
a1 = int(input('Qual o primeiro termo: '))
r = int(input('Qual a razão da PA: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{a1} ► ', end='')
        a1 += r
        cont += 1
    print('Pausa!')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'A progressão terminou com {total} termos!')
