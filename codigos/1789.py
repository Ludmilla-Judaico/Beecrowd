n_lesmas = 0
mais_rapida = 0
velocidades = []
niveis = []

while True:
  try:
    n_lesmas = int(input())
    
    mais_rapida = max(velocidades)
    if(mais_rapida < 10):
      nives.append(1)
    elif(mais_rapida >= 10) and (mais_rapida < 20):
      niveis.append(2)
    elif(mais_rapida >= 20):
      niveis.append(3)

    velocidades = []
  except EOFError:
    break
for elem in niveis:
  print(niveis)