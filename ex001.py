valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos deseja pagar a casa? '))
meses = (anos * 12)
parcelas = valor / meses
print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${parcelas:.2f}')

if parcelas <= salario * 0.3:
    print('\033[32mEmpréstimo condedido!\033[m')
else:
    print('\033[31mEmpréstimo negado!\033[m')
