#matriz
LINHAS, COLUNAS = 12, 12
matriz = []
for i in range(LINHAS):
    matriz.append([0] * COLUNAS)

#entradas
operacao = input()
for i in range(LINHAS):
    for j in range(COLUNAS):
        matriz[i][j] = float(input())

soma = 0
media = 0
inicio = COLUNAS
divisor = 0
if(operacao == 'S'):
    for i in range(1, LINHAS):
        inicio -= 1
        for j in range(inicio, COLUNAS):
            soma += matriz[i][j]
    print(f'{soma:.1f}')

elif(operacao == 'M'):
    for i in range(1, LINHAS):
        inicio -= 1
        for j in range(inicio, COLUNAS):
            soma += matriz[i][j]
            divisor += 1
    media = soma / divisor
    print(f'{media:.1f}')