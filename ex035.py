print('-' * 40)
print(f'{"LOJA ONLINE DA LÍDIA":^40}')
print('-' * 40)
total = caros = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        caros += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if continuar in 'n':
        break
print(f'{" FIM DO PROGRAMA ":-^44}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {caros} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
