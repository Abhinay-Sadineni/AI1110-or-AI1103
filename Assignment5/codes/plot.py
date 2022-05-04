#Used templete given by Prof.GVV sharma
#To plot the binomial distribution
from scipy.stats import binom
import matplotlib.pyplot as plt

n = 3
p = 1/2
r_values = list(range(n + 1))
# list of pmf values
dist = [binom.pmf(r, n, p) for r in r_values ]
# plotting the graph 
plt.xlabel("value of k")
plt.ylabel("Pr(X=k)")
markerline, stemlines, baseline = plt.stem(r_values, dist, '-.')
for i, avg in enumerate(dist):
    plt.annotate('%0.3f' % avg, xy=(i-0.1, avg), xytext=(7,2), color='black', textcoords='offset points')
plt.title("Binomial distribution of X")
plt.savefig("../figs/binomial.png")
plt.show()