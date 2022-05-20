#
# 
# 
import pandas as pd
iris = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv')
#vs
#iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/bezdekIris.data')

print('head',iris.head())

# 
# metadata
# 

print('type',type(iris))
print('info\n',iris.info)
print('keys',iris.keys())
#vs
print('columns',iris.columns)

# 
# may analize each feature
# 
print('mean',iris["petal width"].mean())
print('value_counts\n',iris["petal width"].value_counts().head())
print('shape',iris["petal width"].value_counts().shape)

# 
# descriptive stats
# 

print('describe',iris.describe())

# 
# vs
# 

print('forEach feature')
print(' SUM\n',iris.sum())
print(' mean\n',iris.mean())
print(' min\n',iris.min())
print(' max\n',iris.max())

# 
# excerpts 
#

print('cumsum\n',iris["petal width"].cumsum().head())
#
print('diff\n',iris["petal width"].diff().tail())

# 
# feature means by class
# 

iris.groupby(by = "class").mean()

# 
# sepalwidth mean 
# 

iris.groupby(by = "sepal width").mean().tail()

# 
# 
#

# iris.columns[2]
# vs
iris.groupby(by = iris.columns[2]).mean().head()

# 
#  forEach-feature forEach-label class
# 

iris.groupby(by = "class").min().plot(kind="bar")
#vs
#iris.groupby(by = "class").max().plot(kind="bar")
#vs
#iris.groupby(by = "class").mean().plot(kind="bar")

# 
# 
# 

import matplotlib.pyplot as plt

class_series = iris.groupby('class').size()
class_series.name = ''#distribution
#plt.pie(class_series)
class_series.plot.pie(autopct='%.2f')

# 
# uni-variate
# 

iris.plot()

# 
# bi-variate
# 

iris.plot(kind="scatter", x="sepal width", y="sepal length")

# 
# total correlation (itself)
# 

iris.plot(kind="scatter", x="sepal width", y="sepal width",figsize=(15, 7))

# 
# 
# 

iris.plot(kind="scatter", x="petal width", y="sepal length")

# 
# vs distribution
# 

iris["sepal width"].hist()
iris["sepal width"].value_counts()

# 
# spot outliers
# 

iris.boxplot()

# 
# 
# 

from pandas.plotting import scatter_matrix
scatter_matrix(iris)

# 
# vs
# 

scatter_matrix(iris,diagonal = 'kde')

# 
# 
# 

iris.plot.hist()

# 
# find how many modes
# 

iris.plot.density()

# 
# 
# 

iris.hist()

# 
# create correlation matrix
# 

corr = iris.corr()
print(corr)
#vs
iris.cov()

# 
# the higher (red), the more correlated (cf. diagonal)
#

import statsmodels.api as sm
sm.graphics.plot_corr(corr, xnames=list(corr.columns))
print()

# 
# ranking correlations
# 

corr["sepal length"].sort_values(ascending=False)
