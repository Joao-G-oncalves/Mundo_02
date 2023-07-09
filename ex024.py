from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
sair = 0
while sair != 5:
    somar = n1 + n2
    multiplicar = n1 * n2
    print(f'      [ 1 ] Somar\n'
          f'      [ 2 ] Multiplicar\n'
          f'      [ 3 ] Maior\n'
          f'      [ 4 ] Novos Números\n'
          f'      [ 5 ] Sair do programa')
    sair = int(input('>>>>>>>> Qual a sua opção? '))
    sleep(1)
    maior = n1
    if n2 > n1:
        maior = n2
    if sair != 5:
        if sair == 1:
            print(f'\033[31mA soma entre {n1} e {n2} é igual a {somar}!\033[m')
            print('=-=' * 12)
        elif sair == 2:
            print(f'\033[31mA multiplicação entre {n1} e {n2} é igual a {multiplicar}!\033[m')
            print('=-=' * 12)
        elif sair == 3:
            print(f'\033[31mEntre {n1} e {n2}, o maior é {maior}.\033[m')
            print('=-=' * 12)
        elif sair == 4:
            print(f'\033[31mInforme os números novamente!\033[m')
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
            print('=-=' * 12)
        else:
            print(f'A opção [{sair}] é inválida, tente novamente!')
            print('=-=' * 12)
print(f'Saindo...')
sleep(1)
print('Até a proxima!!!')
