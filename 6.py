import matplotlib.pyplot as plt
from matplotlib import style

style.use("classic")
style.use("bmh")
x=[3,6,7,9,10]
y=[5,10,15,25,3]

plt.title('test scatter')

plt.xlabel('test x')
plt.ylabel('test y')

plt.scatter(x,y)
plt.show()
