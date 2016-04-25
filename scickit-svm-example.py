# ipython notebook

# coding: utf-8

# In[196]:

get_ipython().magic('matplotlib inline')

import matplotlib
from sklearn import svm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")
df.columns = ["sepal_length","sepal_width","petal_length","petal_width","kind"]
df = df.loc[:98,'petal_length':'kind']

color_dict = { 'Iris-setosa':'333', 'Iris-versicolor':'222'}

plt = df.plot(kind='scatter', x='petal_length', y='petal_width',color=[color_dict[i] for i in df['kind']]);
plt.set_title("Basic SVM Example")

# legend


C = 1.0  # SVM regularization parameter
svc = svm.SVC(kernel='linear', C=C)
svc.fit(df.loc[:,'petal_length':'petal_width'], df["kind"])


print(svc.predict([[-0.8, -1]]))

w = svc.coef_[0]
print("coef"+str(w))
print(svc.support_vectors_)
print(svc.support_)
print(svc.n_support_)
print(svc.dual_coef_)
print("intercept:"+str(svc.intercept_[0]))
a = -w[0] / w[1]
print(a)


xx = np.linspace(0,4)
yy = a * xx - svc.intercept_[0] / svc.coef_[0][1]

h0 = plt.plot(xx, yy)



# In[197]:

# import some data to play with
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features. We could
                      # avoid this ugly slicing by using a two-dim dataset
y = iris.target

h = .02  # step size in the mesh

# run the svm
C = 1.0  # SVM regularization parameter
svc = svm.SVC(kernel='linear', C=C)
svc.fit(X, y)

# create a mesh to plot in
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)

# Plot also the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xticks(())
plt.yticks(())
plt.title("Linear svm")

plt.show()

