#import------------------------
import matplotlib.pyplot as plt
import numpy as np

#points in form of arrays---------------------------
A=np.array([0,4])
B=np.array([2,3])
C=np.array([1,1])
D=np.array([2,0])

#reflective matrix used to get reflected points wrt to y-axis----------------------
REF_Y_AXIS = np.array([[-1, 0], [0, 1]])
B_ref= B@REF_Y_AXIS
C_ref= C@REF_Y_AXIS
D_ref= D@REF_Y_AXIS

#plotting points and line segments---------------------------
plt.grid()
x_values = [A[0], B[0]]
y_values = [A[1], B[1]]
plt.plot(x_values, y_values)

x_values = [B[0], C[0]]
y_values = [B[1], C[1]]
plt.plot(x_values, y_values)

x_values = [C[0], D[0]]
y_values = [C[1], D[1]]
plt.plot(x_values, y_values)

x_values = [D[0], D_ref[0]]
y_values = [D[1], D_ref[1]]
plt.plot(x_values, y_values)

x_values = [D_ref[0], C_ref[0]]
y_values = [D_ref[1], C_ref[1]]
plt.plot(x_values, y_values)

x_values = [D[0], D_ref[0]]
y_values = [D[1], D_ref[1]]
plt.plot(x_values, y_values)

x_values = [C_ref[0], B_ref[0]]
y_values = [C_ref[1], B_ref[1]]
plt.plot(x_values, y_values)

x_values = [B_ref[0], A[0]]
y_values = [B_ref[1], A[1]]
plt.plot(x_values, y_values)

#annotation of points----------------------------------------
plt.annotate("A",A,xytext=(0,5),textcoords="offset points")
plt.annotate("B",B,xytext=(0,5),textcoords="offset points")
plt.annotate("C",C,xytext=(0,5),textcoords="offset points",ha='right')
plt.annotate("D",D,xytext=(0,5),textcoords="offset points")
plt.annotate("B'",B_ref,xytext=(0,5),textcoords="offset points")
plt.annotate("C'",C_ref,xytext=(0,5),textcoords="offset points",ha='left')
plt.annotate("D'",D_ref,xytext=(0,5),textcoords="offset points")

#axes and legend------------------------------------------------------
plt.axvline(x=0, c="red", label="line of symmetry with equation x=0")
ax = plt.gca()
ax.set_xlim([-4, 4])
ax.set_ylim([-2, 5])
plt.ylabel('y - axis')
plt.xlabel('x - axis')
plt.legend()
plt.savefig("../Figs/Figure_1.png")
plt.show()
