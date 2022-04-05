import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
  
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

# Dat file data converted to float data type
File_data = np.loadtxt("points.dat", dtype=float)

#points vectors---------------------------
A=File_data [0]
B=File_data [1]
C=File_data [2]
D=File_data [3]
Br=File_data [4]
Cr=File_data [5]
Dr=File_data [6]

#lines just for easy plotting----------------------------------
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
plt.savefig("../Figs/Fig3.png")
plt.show()