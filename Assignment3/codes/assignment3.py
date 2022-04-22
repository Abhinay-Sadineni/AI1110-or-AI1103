#Code by Sadineni abhinay
#April 18, 2022
#Calculate probability of not hitting a boundary

import numpy as np
from numpy import linalg as LA
from numpy import random as RN 

#theoritical probability-------------------
balls = 30
boundries = 6
Pr= (balls - boundries)/balls
print("Theoritically,P(not a Boundary)={}".format(Pr) )


#experimental probability--------------------
#Sample size
N =30

#Generating Samples
x = RN.randint(0, high = 2, size=N)

#Finding the number of 1's and 0's
ppr_1 = np.count_nonzero(x==1)/N
ppr_0 = np.count_nonzero(x==0)/N
print("Practically,P(not a Boundary)={}".format(ppr_0) )






