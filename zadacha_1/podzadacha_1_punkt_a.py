import random
import matplotlib.pyplot as plt
r=0.91
x0=random.random()
n=60
spisok=[]
spisok.append(x0)
for i in range(1,n):
    spisok.append(4*r*spisok[i-1]*(1-spisok[i-1]))
plt.plot(range(n), spisok)

plt.show()