resposta = 's'
cont = soma = media = maior = menor = 0
while resposta in 's':
    n = int(input('Digite um número: '))
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    soma += n
    media = soma / cont
    resposta = str(input('Quer continuar? [S/N] ')).strip().lower()[0]

print(f'Foram digitados {cont} números!'
      f'\nA SOMA entre eles é: {soma}.'
      f'\nO MENOR número foi: {menor}.'
      f'\nO MAIOR número foi: {maior}.'
      f'\nA sua MÉDIA é: {media}.')
