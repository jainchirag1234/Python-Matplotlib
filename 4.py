import matplotlib.pyplot as plt
from matplotlib import style

style.use("dark_background")
style.use("bmh")
numbers=[1,10,15,16,17,19,34,45,56,67,77,78,79,80,81,82,83,84,87,90,91,92,93,94,95,96,98,99,100]
jumps=[0,20,40,60,80,100]

plt.title("test 1 hint")
plt.xlabel("test x label")
plt.ylabel("test y label")
plt.hist(numbers,jumps,histtype="bar")
plt.show()
