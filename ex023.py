from random import randint
from time import sleep
print(f'Olá, sou seu computador!')
sleep(0.5)
print(f'Acabei de pensar em um número entre 0 e 10')
sleep(0.5)
print(f'Será que você consegue adivinhar qual foi?')
pc = randint(0, 10)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input(f'Qual é o seu palpite? '))
    palpite += 1
    print(f'PROCESSANDO...')
    sleep(0.7)
    if jogador > pc:
        print(f'Pensei em um número MENOR que {jogador}.')
    elif jogador < pc:
        print(f'Pensei em um número MAIOR que {jogador}.')
    elif jogador == pc:
        acertou = True
print(f'Acertou com {palpite} tentativas!')
