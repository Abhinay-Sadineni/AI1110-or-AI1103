
import numpy as np
import pandas as pd
from numpy import random as RN 

# Importing data from excel

read = pd.read_excel('../tables/data.xlsx')
raw_data = np.array(read)

#Total number of balls
N = 8
color = np.array(raw_data[0])

pr_1 = color[0]/N

print("Probability that the ball drawn is red ",pr_1)
print("Probability that the ball drawn is not red ",1-pr_1)

#experinmental probability
W=2

x = RN.randint(0, 2, size=W)

x_1 = np.count_nonzero(x==0)
x_2 = np.count_nonzero(x==1)
print("Experimental Probability that the ball drawn  ",x_1/W)
print("Experimental Probability that the ball drawn  ",x_2/W)
