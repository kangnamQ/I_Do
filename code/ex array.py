from numpy.random import randn
from scipy.stats import pearsonr
from scipy.stats import spearmanr

# prepare data
data1 = 20 * randn(1000) + 100
data2 = data1 + (10 * randn(1000) + 50)

# calculate Pearson's correlation
corr1, _ = pearsonr(data1, data2)
print('Pearsons correlation: %.3f' % corr1)

# calculate spearman's correlation
corr2, _ = spearmanr(data1, data2)
print('Spearmans correlation: %.3f' % corr2)