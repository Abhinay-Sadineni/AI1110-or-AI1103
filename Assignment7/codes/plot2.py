from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

#Number of trials, probability of success
n = 6
p = 1/2

#Binomial Random Variable
rv = binom(n, p)

#X axis
x_val = np.arange((n+1))

#PMF Values (Y axis)
pmf_val = rv.pmf(x_val)

#Plot
plt.plot(x_val, pmf_val, 'ro',)
plt.stem(x_val, pmf_val, linefmt='r-', markerfmt='ro', basefmt='k--')

plt.legend(loc = 'best', frameon = True)
plt.title("Binomial distribution of X")
plt.savefig("../figs/binomial1.png")

plt.show()
