import scipy.stats

#find Chi-Square critical value
print(scipy.stats.chi2.ppf(1-0.025, df=10))
print(scipy.stats.chi2.ppf(0.025, df=10))
