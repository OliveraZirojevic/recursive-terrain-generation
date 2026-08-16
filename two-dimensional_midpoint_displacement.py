import numpy as np
import random
import matplotlib.pyplot as plt


def getSkyline(niz, a, b):
  if abs(b - a) <= 1:
    return
#računanje i zadavanje vrednosti midpointu
  midpoint = (a+b)//2
  hRandom =random.uniform(-(b+1)/2, (b + 1)/2)/5# random displacement je u opsegu pola dužine niza
  niz[midpoint] += hRandom

  getSkyline(niz, a, midpoint)
  getSkyline(niz, midpoint, b)

lista = np.zeros(17)
hRandom =random.uniform(-len(lista)/2, len(lista)/2) /  3# random displacement je u opsegu pola dužine niza
lista[len(lista)//2] += hRandom
print(lista)

getSkyline(lista, 0, len(lista) - 1)
print(lista)
fig = plt.plot(lista, color = "black")


plt.show()