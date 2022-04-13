#import------------------------
from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA

#observations and plotting them in graph------------------
A=np.array([1,7])
B=np.array([2,6])
C=np.array([3,5])
D=np.array([4,4])
E=np.array([5,3])

P=[A,B,C,D,E]
for V in P:
 plt.scatter(V[0],V[1],color="blue")

# Dat file data converted to float data type(coefficents)-------
File_data = np.loadtxt("coefficents.dat", dtype=float)
a_1=File_data [0]
a_0=File_data [1]


#plotting line using coefficents ---------------------------
plt.grid()
x=np.arange(0,9,1)
y=a_0+(a_1)*x
plt.plot(x,y,label="line of regrssion x+y=8 ",color="red")


plt.annotate("A",A,xytext=(0,5),textcoords="offset points")
plt.annotate("B",B,xytext=(0,5),textcoords="offset points")
plt.annotate("C",C,xytext=(0,5),textcoords="offset points",ha='right')
plt.annotate("D",D,xytext=(0,5),textcoords="offset points")
plt.annotate("E",E,xytext=(0,5),textcoords="offset points")

ax = plt.gca()
ax.set_xlim([0,8])
ax.set_ylim([0,8])
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.savefig("../figs/fig1.png")
plt.show()