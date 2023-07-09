valor = int(input('Qual valor você quer sacar? R$ '))
ced = 100
total = 0
while True:
    if valor >= ced:
        valor -= ced
        total += 1
    else:
        if total > 0:
            print(f'Total de {total} cédulas de R${ced:3}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total = 0
        if valor == 0:
            break
