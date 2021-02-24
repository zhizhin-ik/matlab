import random
import numpy as np
import matplotlib.pyplot as plt
n = 1000

rlist = []

for j in range(1, 1000):
    x0 = random.random()
    r = j*0.001
    spisok = []
    spisok.append(x0)
    for i in range(1,n):
        x = 4*r*spisok[i-1]*(1-spisok[i-1])
        spisok.append(x)
    plt.scatter(r, x, s=0.1, c='red')

plt.show()
