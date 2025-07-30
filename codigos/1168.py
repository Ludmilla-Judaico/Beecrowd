testes = int(input())
qntd_leds = {'0':6, '1':2, '2':5, '3':5,
              '4':4, '5':5, '6':6, '7':3, '8':7, '9':6}

soma = 0
for i in range(testes):
    numero = input()
    for e in numero:
        for elem in qntd_leds.keys():
            if(e == elem):
                soma += qntd_leds[elem]
    print(f'{soma} leds')
    soma = 0