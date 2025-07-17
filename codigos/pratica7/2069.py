campo = []
for i in range(6):
    campo.append([0] * 8)

qntd_bombas = int(input())
for i in range(qntd_bombas):
    x, y = map(int, input().split())
    campo[x][y] = 'bomba'

area_x, area_y = map(int, input().split())

cima_x, cima_y = area_x - 1, area_y
baixo_x, baixo_y = area_x + 1, area_y
esq_x, esq_y = area_x, area_y - 1
dir_x, dir_y = area_x, area_y + 1
superior_esq_x, superior_esq_y  = area_x - 1, area_y - 1
inferior_esq_x, inferior_esq_y = area_x + 1, area_y - 1
superior_dir_x, superior_dir_y  = area_x - 1, area_y + 1
inferior_dir_x, inferior_dir_y = area_x + 1, area_y + 1

if(campo[area_x][area_y] != 'bomba'):
    if(campo[cima_x][cima_y] == 'bomba'):
            campo[area_x][area_y] += 1

    if(campo[baixo_x][baixo_y] == 'bomba'):
            campo[area_x][area_y] += 1

    if(campo[esq_x][esq_y] == 'bomba'):
            campo[area_x][area_y] += 1

    if(campo[dir_x][dir_y] == 'bomba'):
            campo[area_x][area_y] += 1

    if(campo[superior_dir_x][superior_dir_y] == 'bomba'):
            campo[area_x][area_y] += 1

    if(campo[superior_esq_x][superior_esq_y] == 'bomba'):
            campo[area_x][area_y] += 1

    if(campo[inferior_dir_x][inferior_dir_y] == 'bomba'):
            campo[area_x][area_y] += 1

    if(campo[inferior_esq_x][inferior_esq_y] == 'bomba'):
            campo[area_x][area_y] += 1

if(campo[area_x][area_y] == 'bomba'):
    print('B')
elif(campo[area_x][area_y] == 0):
    print('X')
else:
    print(campo[area_x][area_y])