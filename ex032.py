cont = 0
while True:
    n = int(input('Digite um número para saber sua tabuada: '))
    print('-' * 40)
    if n < 0:
        break
    while cont < 10:
        cont += 1
        print(f'{n} x {cont:2} = {n * cont:3}')
    cont = 0
    print('-' * 40)
print(f'Programa tabuada encerrado, volte sempre!')
