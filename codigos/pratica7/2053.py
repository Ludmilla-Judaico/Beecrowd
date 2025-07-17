tela = []
for i in range(8):
    tela.append([0] * 4)

x, y = 0, 0

for i in range(20):
    x, y = map(int, input(). split( ))
    tela[x][y] += 1

maior = max(max(i) for i in tela)
for i in range(8):
    for j in range(4):
        if(tela[i][j] == maior):
            print(f'{i} {j}')