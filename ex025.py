n = int(input('Digite um número para saber seu fatorial: '))
m = 1
print(f'Calculando {n}! =', end='')
while n > 0:
    print(f' {n} ', end='')
    if n > 1:
        print(f' x ', end='')
    else:
        print(f' = ', end='')
    m *= n
    n -= 1
print(f'{m}.')
