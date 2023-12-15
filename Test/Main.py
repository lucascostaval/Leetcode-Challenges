from typing import List

def somar(x, y):
    return x+y

def media(notas: List[int]):
    tamanho = len(notas)
    tot = 0
    for nota in notas:
        tot = tot+nota
    m = tot/tamanho
    return m

notas = [3, 9, 5, 4, 0]
z = somar(media(notas), 1)
print(z)
if z < 7:
    print("Reprovado. Melhore")
    if z <= 0:
        print("kkkk")
else:
    print("Aprovado. Jogabilidade avançada")