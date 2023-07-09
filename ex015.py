c = 0
s = 0
for cont in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        c += 1
print(f'Foram computados {c} números pares e a soma entre ele é de {s}!')
