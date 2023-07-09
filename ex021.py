idade_total = 0
homem = 0
mulher = 0
idade = 0
maisvelho = 0
nome = ''
idadedohomem = 0
for pessoa in range(1, 5):
    print(f'---- {pessoa}ª PESSOA ----')
    Nome = str(input(f'Nome: ')).strip().lower()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F]: ')).strip()
    idade_total += idade
    if sexo in 'Mm' and pessoa == 1:
        homem += 1
        maisvelho = idade
        nome += Nome
        idadedohomem += idade
    elif sexo in 'Mm' and idade > maisvelho:
        maisvelho = idade
        nome += Nome
        idadedohomem += idade

    if sexo in 'Ff' and idade < 20:
        mulher += 1


m_idade = idade_total / 4
print(f'A média de idade das 4 pessoas é de {m_idade:.0f} anos!')
print(f'O número de mulheres com menos de 20 anos é de {mulher}!')
print(f'E o homem mais velho é o Sr. {nome.title()} com {idadedohomem} anos!')
