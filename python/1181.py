linha = int(input())
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

if(operacao == 'S'):
    for j in range(QTD_MATRIZ):
        soma += matriz[linha][j]
    print(f'{soma:.1f}')

elif(operacao == 'M'):
    for j in range(QTD_MATRIZ):
        soma += matriz[linha][j]
    media = soma / QTD_MATRIZ
    print(f'{media:.1f}')