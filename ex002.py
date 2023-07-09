n = int(input('Digite um número inteiro qualquer: '))
a = int(input('Escolha uma das bases para conversão: \n'
              '[1] - para binario,\n'
              '[2] - para octal ou\n'
              '[3] - para hexadecimal \n'
              'Sua Opção: '))
if a == 1:
    print(f'{n} em binário equivale a {bin(n)[2:]}')
elif a == 2:
    print(f'{n} em octal equivale a {oct(n)[2:]}')
elif a == 3:
    print(f'{n} em hexadecimal equivale a {hex(n)[2:]}')
else:
    print(f'Opção [{a}] inválida.')
