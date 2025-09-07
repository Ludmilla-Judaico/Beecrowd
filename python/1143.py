qntd = int(input())

contador = 0

for linha in range(qntd):
    contador += 1
    quadrado = contador ** 2
    cubo = contador ** 3
    print(f'{contador} {quadrado} {cubo}')
