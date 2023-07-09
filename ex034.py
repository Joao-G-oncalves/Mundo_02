maior18 = homens = mulheres = 0
while True:
    print('-' * 40)
    print(f'{" CADASTRE UMA PESSOA ":=^40}')
    print('-' * 40)
    idade = int(input('Idade: '))
    if idade > 18:
        maior18 += 1
    sexo = ' '
    while sexo not in 'fm':
        sexo = str(input('Sexo: [M/F] ')).strip().lower()[0]
    print('-' * 40)
    if sexo in 'm':
        homens += 1
    if sexo in 'f' and idade < 20:
        mulheres += 1
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if continuar in 'n':
        print(f'{"FIM DO PROGRAMA":~^40}')
        break
print(f'Total de pessoas com mais de 18 anos: {maior18}\n'
      f'Ao todo temos {homens} homens cadastrados.\n'
      f'Temos {mulheres} mulheres com menos de 20 anos.')
