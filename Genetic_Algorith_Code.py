# -*- coding: utf-8 -*-
"""palipali.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_FH3rJKF7hAdGRhcDIAHn-1ExSd778hG
"""

import random
import math

def createpopulasi(jumlahpopulasi):
  populasi = []
  for i in range(jumlahpopulasi) : 
    kromosom = []
    for j in range(9) : 
      kromosom.append(random.randint(0,9))
    populasi.append(kromosom)

  return populasi

def decoding(rmax, rmin, g):
    x = [2**-i for i in range(1, len(g)+1)]
    return rmin + ((rmax - rmin) / sum(x) * sum([g[i] * g[i] for i in range(len(g))]))

def hitungfitness(x, y): #menghitung nilai fitness berdasarkan rumus yang sudah diberi di soal
         return 1/ ((math.cos(x) + math.sin(y)) ** 2 / x**2 + y**2) + 0.0001

def seleksiturnamen(populasi):
    tournament = []
    fitness = []
    max = 0
    pemenang = 0
    for i in range(5):
      tournament.append(random.choice(populasi))
      x = decoding(3.0, -2.0, tournament[i][:5])
      y = decoding(2.0, -1.0, tournament[i][5:])
      fitness.append(hitungfitness(x, y))
      if fitness[i] > max:
        max = fitness[i]
        pemenang = 1

    return pemenang

def crossover(ortu1, ortu2):
    pc = random.random()
    anak1 = ()
    anak2 = ()
    randint = random. uniform(0.0, 1.0)
    titikPotong = int(round(random.uniform(0, 5)))
    if randint <= pc:
        anak1 = ortu1[:titikPotong] + ortu2[titikPotong:]
        anak2 = ortu2[:titikPotong] + ortu1[titikPotong:]
    else :
     anak1 = ortu1
     anak2 = ortu2
    return anak1, anak2

def sort_fitness(fitness): #untuk mengurutkan fitness
    return sorted(range(len(fitness)), key=lambda k: fitness[k], reverse=True)

def mutasi(a):
    pm = 0.5
    randnum = random.uniform(0.0, 1.0)
    if randnum > (1 - pm):
       posisi_mutasi = random.randint(0, len(a) - 1)
       if a[posisi_mutasi] == 1:
          a[posisi_mutasi] = 0
       else:
            a[posisi_mutasi] = 1

def Steadystate(gabungan):
    fitness = []
    for i in range(len(gabungan)):
       if gabungan[i] != None:
         x = decoding(2, -1, gabungan[i][:5])
         y = decoding(1, -1, gabungan[i][5:])
         fitness.append(hitungfitness(x, y))

    steadystate_list = sort_fitness(fitness)
    population = []

    for j in range(jumlahpopulasi):
        population.append(gabungan[steadystate_list[j]])
    return population, fitness

"""Main program




"""

JumlahGenerasi = int(input("Jumlah generasi yang diinginkan : "))
jumlahpopulasi = int(input("Jumlah populasi yang diinginkan : "))
population = createpopulasi(jumlahpopulasi)
for i in range(JumlahGenerasi):
    fitness = []
    anak = []
    for j in range(jumlahpopulasi):
        orangtual = seleksiturnamen(population)
        orangtua2 = seleksiturnamen(population)
        anak1 = population[orangtual]
        anak2 = population[orangtua2]
        crossover(anak1, anak2)
        anak1 = mutasi(anak1)
        anak2 = mutasi(anak2)
        anak. append(anak1)
        anak. append (anak2)
    gabungan = population + anak
    population, fitness = Steadystate(gabungan)

    print("----------------------------------------")                      
    print("Generasi ke", i+1)
    print('Nilai fitness: ', fitness[0])
    print('x:', decoding(5, -5, population[0][:5]))
    print('y:', decoding(5, -5, population[0][5:]))
    print()
    print('Kromosom terbaiknya adalah : ', population[0])
    print('Nilai fitness: ', fitness[0])
    print("----------------------------------------")
    print("\n")