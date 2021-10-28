import numpy as np
import matplotlib.pyplot as plt
"""
notas_pedro = [8, 9, 7, 8]
notas_maria = [5, 10, 6, 9]
notas_jose = [7, 7, 5, 8]

barWidth = 0.25

plt.figure(figsize=(10, 5))

r1 = np.arange(len(notas_pedro))
r2 = [x + barWidth for x in r1 ]
r3 = [x + barWidth for x in r2 ]


plt.bar(r1, notas_pedro, color="#6A5ACD", width=barWidth, label="Pedro")
plt.bar(r2, notas_maria, color="#6495ED", width=barWidth, label="Maria" )
plt.bar(r3, notas_jose, color="#00BFFF", width=barWidth, label="Jose")

plt.xlabel("Provas")
plt.xticks([ r + barWidth for r in range(len(notas_pedro)) ], ["Prova 1", "Prova 2", "Prova 3", "Prova 4"])
plt.ylabel("Notas")
plt.title("Representação das notas de 3 alunos em 4 provas do semestre")

plt.legend()
plt.show()
"""

barWidth = .1

ptenc_corsa = [200, 350, 556]
ptenc_celta = [125, 233, 440]
ptenc_camaro = [1500, 2708, 2880]
ptenc_ferrari = [3000, 3500, 4100]


#cria uma série de números em função da primeria lista[]
pos1 =  np.arange(len(ptenc_corsa))

#Cria uma lista de valores posteriormente a lagura da barra com o valor do antecessor
pos2 = [ barWidth + x for x in pos1 ]
pos3 = [ barWidth + x for x in pos2 ]
pos4 = [ barWidth + x for x in pos3 ]

#cria uma lista de carros com as listas já criadas
cars = [
  ptenc_corsa,
  ptenc_celta,
  ptenc_camaro,
  ptenc_ferrari
]

#cria uma lista de posições com as listas anteriores
position = [
  pos1, pos2, pos3, pos4
]

#cria um lista de cores
colors = [
  "#AFFF",
  "#345645",
  "#321",
  "#643"
]

#Define o tamanho da imagem
plt.figure(figsize=(10, 5))

#Com as três listas ciradas, cars, position, colors, é usado um for zip para desintegrar cada uma
#E criar uma plotagem para cada barra
for (pos, color, car) in zip(position, colors, cars):
  plt.bar(pos, car,  color=color, width=barWidth, label="Label")

#Mostra os os gráficos
plt.show()


