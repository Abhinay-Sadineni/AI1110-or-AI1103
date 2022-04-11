#import------------------------
from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA

#for creating lines---------------
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

A=np.array([1,7])
B=np.array([2,6])
C=np.array([3,5])
D=np.array([4,4])
E=np.array([5,3])

P=[A,B,C,D,E]
for x in P:
 plt.scatter(x[0],x[1],color="blue")

O=np.array([0,8])
R=np.array([8,0])
x_OR= line_gen(O,R)

#plotting points and lines ---------------------------
plt.grid()

plt.plot(x_OR[0,:],x_OR[1,:],label="line of regression x+y=8",color="red")

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