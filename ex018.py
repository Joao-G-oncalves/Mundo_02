'''frase = str(input('Digite uma frase para vermos se ela pode ser um palíndromo: ')).strip().lower()
frasesemespaco = frase.replace(' ', '')
invert = (frasesemespaco[::-1])
print(f'O inverso de "{frase.title()}" é {invert.upper()},')
if frasesemespaco == invert:
   print('então ela é um palíndromo!')
else:
   print(f'então esta frase NÃO é um palíndromo!')'''

frase = str(input('Digite uma frase para vermos se ela pode ser um palíndromo: ')).strip().lower().split()
junto = ''.join(frase)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(inverso)
