operacao = input()

QTD_MATRIZ = 12
matriz = []
for i in range(QTD_MATRIZ):
    matriz.append([0] * QTD_MATRIZ)

for i in range(QTD_MATRIZ):
    for j in range(QTD_MATRIZ):
        matriz[i][j] = float(input())

soma = 0
media = 0
contador = 0

if(operacao == 'S'):
    for i in range(QTD_MATRIZ):
        for j in range(QTD_MATRIZ):
            if(i < j):
                soma += matriz[i][j]
    print(f'{soma:.1f}')

elif(operacao == 'M'):
    for i in range(QTD_MATRIZ):
        for j in range(QTD_MATRIZ):
            if(i < j):
                soma += matriz[i][j]
                contador += 1
    media = soma / contador
    print(f'{media:.1f}')