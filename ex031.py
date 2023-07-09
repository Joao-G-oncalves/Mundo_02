cont = soma = 0
while True:
    n = int(input('Digite um valor: [999 para parar] '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Foram digitados {cont} números e sua soma é igual a {soma}!')
