import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')
style.use('bmh')
x1=[2,3,6]
y1=[3,6,9]

x2=[4,8,12]
y2=[6,12,10]

x3=[5,10,15]
y3=[7,14,10]

plt.bar(x1,y1)
plt.bar(x2,y2)
plt.bar(x3,y3)

plt.title("test graph")

plt.xlabel("test x name")
plt.ylabel("test y name")
plt.show()
