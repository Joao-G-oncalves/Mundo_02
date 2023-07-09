from random import randint
print('=-' * 25)
print('Vamos jogar Par ou Ímpar')
total = 0
while True:
    pc = randint(0, 10)
    print('=-' * 25)
    jogador = int(input('Digite um valor: '))
    escolha = ' '
    while escolha not in 'pi':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().lower()[0]
    soma = jogador + pc
    if escolha in 'p':
        escolha = 'PAR'
    elif escolha in 'i':
        escolha = 'ÍMPAR'
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print('-' * 50)
    print(f'Você jogou {jogador} e o computador {pc}. Total de {soma} DEU {resultado}')
    print('-' * 50)
    if escolha == resultado:
        total += 1
        print('Você venceu!'
              '\nVamos jogar novamente...')
    else:
        break
print(f'GAME OVER!! Você venceu {total} vezes.')
