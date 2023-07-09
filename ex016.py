a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
decimo = a1 + (10 - 1) * r
for c in range(a1, decimo + r, r):
    print(c, end=', ')
print('ACABOU!')
