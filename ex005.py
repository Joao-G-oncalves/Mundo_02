n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
n3 = float(input('Terceita Nota: '))
n4 = float(input('Quarta Nota: '))
m = (n1 + n2 + n3 + n4)/4
if m < 5:
    print(f'Reprovado, pois sua média foi {m:.2f}!')
elif 5.0 <= m <= 6.9:
    print(f'RECUPERAÇÃO, pois sua média foi {m:.2f}!')
else:
    print(f'Aprovado, pois sua média foi {m:.2f}!')
