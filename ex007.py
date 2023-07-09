a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print(f'Pode ser feito um triangulo e ele é:', end=' ')
    if a == b == c:
        print(f'EQUILATERO!')
    elif a != b != c != a:
        print(f'ESCALENO!')
    elif a == b != c or b == c != a or c == a != b:
        print(f'ISOSCELES!')
else:
    print(f'Não pode ser feito um triângulo!')
