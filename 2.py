import matplotlib.pyplot as plt
from matplotlib import style

style.use("dark_background")
style.use("bmh")
x=[2,4,8]
y=[1,3,5]

x1=[1,5,9]
y1=[3,6,8]

plt.plot(x,y)
plt.plot(x1,y1)
plt.title("Test")
plt.xlabel("Test x values")
plt.ylabel("Test y values")

plt.show()
