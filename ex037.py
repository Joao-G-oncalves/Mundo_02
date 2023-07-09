from random import sample


def palavra(txt):
    x = sample(txt, len(txt))
    y = ''.join(x).strip().upper()
    return y


p = str(input('Digite qualquer palavra: '))
print(palavra(p))
