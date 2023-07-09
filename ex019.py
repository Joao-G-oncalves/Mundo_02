from datetime import date
menor = 0
maior = 0
for c in range(1, 8):
    idade = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if date.today().year - idade < 21:
        menor += 1
    else:
        maior += 1
print(f'nessa lista {menor} pessoas são menores de 21 anos e {maior} são maiores de 21 anos '
      f'no ano de {date.today().year}!')
