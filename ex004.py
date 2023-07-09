from datetime import date
ano = int(input('Digite o ano que você nasceu: '))
anoatual = date.today().year
print(f'De acordo com sua idade: {anoatual - ano}')
diferenca = anoatual - ano - 18
diferenca2 = - anoatual + ano + 18

if anoatual - ano < 18:
    print(f'Você vai se alistar daqui há {-diferenca} ano(s).')
elif anoatual - ano == 18:
    print(f'Esse é o ano do seu alistamento.')
elif anoatual - ano > 18:
    print(f'Você se alistou, ou deveria, há {diferenca} ano(s) atrás.')
