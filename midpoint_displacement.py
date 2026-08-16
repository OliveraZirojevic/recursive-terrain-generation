import numpy as np
import matplotlib.pyplot as plt
import random

#r1 i c1 su koordinate gornjeg levog, a r2 i c2 donjeg desnog ugla dela nad kojim operišem
def getLandscape(arr, r1, c1, r2, c2):
  #base case (algoritam se zaustavlja kada je neka od str kvadrata nad kojim operiše manja ili jednaka 1)
  if abs(r1 - r2) <= 1 or abs(c1 - c2) <= 1:
    return
  #određivanje midpointa
  mr = (r1 + r2) //2 #midred
  mc = (c1 + c2) // 2 # midkolona

  # diamond step
  arr[mr, c1] = (arr[r1, c1] + arr[r2, c1]) / 2 + random.uniform(-0.2, 0.2)
  arr[mr, c2] = (arr[r2, c2] + arr[r1, c2]) / 2 + random.uniform(-0.2, 0.2)
  arr[r1, mc] = (arr[r1, c2] + arr[r1, c1]) / 2 + random.uniform(-0.2, 0.2)
  arr[r2, mc] = (arr[r2, c2] + arr[r2, c1]) / 2 + random.uniform(-0.2, 0.2)

 #midpoint displacement (square step)
  arr[mr, mc] = (arr[mr, c1] + arr[mr, c2] + arr[r1, mc] + arr[r2, mc]) / 4 +  random.uniform(-0.2, 0.2)

  #rekurzija 4x square step
  getLandscape(arr, r1, c1, mr, mc)
  getLandscape(arr, r1, mc, mr, c2)
  getLandscape(arr, mr, c1, r2, mc)
  getLandscape(arr, mr, mc, r2, c2)


#pravljenje liste
def make_array(n):
  arr = np.zeros(n*n)
  arr = arr.reshape(n, n)
  return arr
lista = make_array(9)
#setovanje pocetnih vrednosti coskova
lista[0, 0] = 2
lista[0, len(lista) - 1] = lista[0, 0]
lista[len(lista) - 1, 0] = lista[0, 0]
lista[len(lista) - 1, len(lista) - 1] = lista[0, 0]
getLandscape(lista, 0, 0, len(lista) - 1, len(lista) - 1)
plt.imshow(lista, interpolation = "bicubic", cmap = "prism")