import matplotlib.pyplot as plt
r=0.958
x0=0.5
x1=0.5
n=300
spisok_1=[]
spisok_1.append(x0)
spisok_2=[]
spisok_2.append(x1)
for i in range(1,n):
    x=4*r*spisok_1[i-1]*(1-spisok_1[i-1])
    spisok_1.append(x)

for i in range(1,n):
    x = 4 * r * spisok_2[i - 1] * (1 - spisok_2[i - 1])
    x = x / 10
    x = x * 10
    # x = x / 16
    # x = x * 16
    # x = x / 128
    # x = x * 128
    spisok_2.append(x)
plt.plot(range(n), spisok_1)
plt.plot(range(n), spisok_2)

plt.show()

