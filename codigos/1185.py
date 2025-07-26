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
contador = 0
divisor = 0
if(operacao == 'S'):
    for i in range(LINHAS):
        contador += 1
        for j in range(COLUNAS - contador):
            soma += matriz[i][j]
    print(f'{soma:.1f}')

elif(operacao == 'M'):
    for i in range(LINHAS):
        contador += 1
        for j in range(COLUNAS - contador):
            soma += matriz[i][j]
            divisor += 1
    media = soma / divisor
    print(f'{media:.1f}')