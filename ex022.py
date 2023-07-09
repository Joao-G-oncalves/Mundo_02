sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'Mm' 'Ff':
    sexo = str(input('Sexo errado, informe novamente: ')).strip().upper()[0]
if sexo in 'Mm':
    sexo = 'Masculino'
elif sexo in 'Ff':
    sexo = 'Feminino'
print(f'Sexo {sexo}, registrado com sucesso!')
