from datetime import date
nome = str(input('Olá, atleta digite seu nome: '))
nascimento = int(input(f'Olá, {nome}! me informe o ano que você nasceu: '))
ano = date.today().year
idade = ano - nascimento
print(f'{nome} de acordo com sua idade {idade} \nSua categoria é:', end=' ')

if idade <= 9:
    print(f'MIRIM')
elif 9 < idade <= 14:
    print(f'INFANTIL')
elif 14 < idade <= 19:
    print(f'JUNIOR')
elif 19 < idade <= 20:
    print(f'SÊNIOR')
elif 20 < idade:
    print(f'MASTER')
