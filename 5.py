import matplotlib.pyplot as plt
from matplotlib import style

style.use("classic")
style.use("bmh")
food=["pizza","ice-cream","burger"]
sales=[20,10,30]
color=["blue","brown","yellow"]

plt.pie(sales,labels=food,colors=color)

plt.title("example food")

plt.show()
