a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))

if a > b:
    print(f'O primeiro valor {a} é maior que {b}!')
elif b > a:
    print(f'O segundo valor {b} é maior que {a}!')
else:
    print(f'Não existe valor maior, os dois são iguais!')
