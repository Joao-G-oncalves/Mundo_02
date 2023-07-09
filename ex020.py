maior = 0
menor = 0
soma = 0
for c in range(1, 6):
    peso = float(input(f'Qual o peso da {c}ª pessoa? '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
            print(f'O maior mudou para {peso}Kg.')
        if peso < menor:
            menor = peso
            print(f'O menor mudou para {peso}Kg.')
    soma += peso
print(f'o maior peso lido foi de {maior}Kg.')
print(f'o menor peso lido foi de {menor}Kg.')
print(f'A soma de todos os pesos foram {soma}Kg!')
