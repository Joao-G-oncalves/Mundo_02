s = 0
c = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        c += 1
        s += cont
print(f'A soma de todos os números impáres divisiveis por 3 entre 1 e 500 é = {s}, foram contados {c} números')
