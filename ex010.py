from random import choice
from time import sleep
print('=========================================================')
print(f'                         \033[1:36mJokenpô\033[m')
print('=========================================================')
jogador = str(input(f'\033[33mEscolha pedra, papel ou tesoura: \033[m')).strip().lower()
lista = ['Pedra', 'Papel', 'Tesoura']
PC = choice(lista)
print('_'*57)
print(f'JO...')
sleep(1)
print(f'      KEN...')
sleep(1)
print(f'             PÔ!!!')
print('_'*57)

print(f'\033[34mEu escolhi \033[31m{PC}\033[34m, e você escolheu \033[32m{jogador.capitalize()}\033[m!')

if PC == 'Pedra' and jogador == 'tesoura':
    print(f'\033[31mPC WIN\033[m')
elif PC == 'Pedra' and jogador == 'papel':
    print(f'\033[32mJogador Venceu!\033[m')
elif PC == 'Pedra' and jogador == 'pedra':
    print(f'\033[35mEmpate!\033[m')
elif PC == 'Tesoura' and jogador == 'pedra':
    print(f'\033[32mJogador Venceu!\033[m')
elif PC == 'Tesoura' and jogador == 'papel':
    print(f'\033[31mPC WIN\033[m')
elif PC == 'Tesoura' and jogador == 'tesoura':
    print(f'\033[35mEmpate!\033[m')
elif PC == 'Papel' and jogador == 'papel':
    print(f'\033[35mEmpate!\033[m')
elif PC == 'Papel' and jogador == 'tesoura':
    print(f'\033[32mJogador Venceu!\033[m')
elif PC == 'Papel' and jogador == 'pedra':
    print(f'\033[31mPC WIN\033[m')
else:
    print('Escolha apenas uma opção, tente novamente!')
