from math import pow
peso = float(input('Digite seu peso: Kg '))
altura = float(input('Digite sua altura: M '))
IMC = peso / pow(altura, 2)
if IMC < 18.5:
    print(f'Seu IMC é de {IMC:.2f} e você está abaixo do peso!')
elif 18.5 <= IMC < 25:
    print(f'Seu IMC é de {IMC:.2f} e você está no peso ideal!')
elif 25 <= IMC < 30:
    print(f'Seu IMC é de {IMC:.2f} e você está em sobrepeso!')
elif 30 <= IMC < 40:
    print(f'Seu IMC é de {IMC:.2f} e você está em obesidade!')
else:
    print(f'Seu IMC é de {IMC:.2f} e você está em obesidade mórbida!')
