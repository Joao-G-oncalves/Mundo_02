preco = float(input('Qual o preço do produto? R$ '))
dinheiro = preco - (preco * 0.1)
cartao = preco - (preco * 0.05)
cartao2x = preco
cartao3x = preco + (preco * 0.2)
print(f'FORMAS DE PAGAMENTO\n'
      f'[1] à vista dinheiro/cheque;\n'
      f'[2] á vista no cartão;\n'
      f'[3] 2x no cartão;\n'
      f'[4] 3x ou mais no cartão.')
pagamento = int(input('Qual é a opção? '))
if pagamento == 1:
    print(f'Você pagará R${dinheiro:.2f}, incluso 10% de desconto!')
elif pagamento == 2:
    print(f'Você pagará R${cartao:.2f}, incluso 5% de desconto!')
elif pagamento == 3:
    print(f'Você pagará R${cartao2x:.2f}, preço normal sem desconto!')
elif pagamento == 4:
    parcelas = int(input('Quantas Parcelas? '))

    print(f'Sua compra será parcelada em {parcelas}x de R${cartao3x/parcelas:.2f} com juros!')
    print(f'Sua compra de R${preco:.2f} vai custar R${cartao3x:.2f} no final')
else:
    print(f'Opção inválida, tente novamente!')
