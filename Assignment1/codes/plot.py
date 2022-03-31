#import------------------------
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


#this code excatly follows the theory------------------------------
#points vectors---------------------------
A=np.array([0,4])
B=np.array([2,3])
C=np.array([1,1])
D=np.array([2,0])

# here Mr is used in place of M'
#reflection vector and staced matrix ----------------------
R = np.array([[-1,0], [0, 1]])
M = np.array([[2,1,2],[3,1,0]])
Mr=R@M

#Br in place of B'
#Cr in place of C'
#Dr in place of D'
#gettting column vectors from the matrix  to get reflected points--------------------
Br=Mr.T[0]
Cr=Mr.T[1]
Dr=Mr.T[2]

#lines vector----------------------------------
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_D_Dr=line_gen(D,Dr)
x_Dr_Cr=line_gen(Dr,Cr)
x_Cr_Br=line_gen(Cr,Br)
x_Br_A =line_gen(Br,A)

#plotting points and lines ---------------------------
plt.grid()

plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_BC[0,:],x_BC[1,:])
plt.plot(x_CD[0,:],x_CD[1,:])
plt.plot(x_D_Dr[0,:],x_D_Dr[1,:])
plt.plot(x_Dr_Cr[0,:],x_Dr_Cr[1,:])
plt.plot(x_Cr_Br[0,:],x_Cr_Br[1,:])
plt.plot(x_Br_A[0,:],x_Br_A[1,:])

#annotation of points----------------------------------------
plt.annotate("A",A,xytext=(0,5),textcoords="offset points")
plt.annotate("B",B,xytext=(0,5),textcoords="offset points")
plt.annotate("C",C,xytext=(0,5),textcoords="offset points",ha='right')
plt.annotate("D",D,xytext=(0,5),textcoords="offset points")
plt.annotate("B'",Br,xytext=(0,5),textcoords="offset points")
plt.annotate("C'",Cr,xytext=(0,5),textcoords="offset points",ha='left')
plt.annotate("D'",Dr,xytext=(0,5),textcoords="offset points")

#axes and legend------------------------------------------------------
plt.axvline(x=0, c="red", label="line of symmetry $x=0$")
ax = plt.gca()
ax.set_xlim([-4, 4])
ax.set_ylim([-2, 5])
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.show()