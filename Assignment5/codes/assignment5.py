
#To find the probability of an event using the binomial distribution

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom




#Simlen
simlen=1000

#Number of times coin tossed
n = 3

#Probability of getting a head
p = 1/2


#Theoretical probability Here k is the number of heads
print("Theoreticial probability of the events:")
k=0
print("P(A)={}".format(binom.pmf(k, n, p)))
k=1
print("P(B)={}".format(binom.pmf(k,n,p)))
print("P(C)={}".format(1-binom.cdf(k,n,p)))



#Simulating the probability using  the binomial random variable
data_binom = binom.rvs(n,p,size=simlen)
#Simulating the event of tossing a coin three times
#checking probability condition
err_A = np.nonzero(data_binom==0)
err_B = np.nonzero(data_binom==1)
err_C = np.nonzero(2<=data_binom)
#computing the probability
err_n = np.size(err_A)
err_w = np.size(err_B)
err_q = np.size(err_C)
print("Experimental probability of the events:")
print(err_n/simlen)
print(err_w/simlen)
print(err_q/simlen)
print((err_n+err_w+err_q)/simlen)
