from sklearn import preprocessing
import numpy as np
from sklearn.preprocessing import StandardScaler
import math

x = np.array([[3., -1., 2., 613.],
              [2., 0., 0., 232],
              [0., 1., -1., 113],
              [1., 2., -3., 489]])

#MinMaxScaler() 归一化到[0,1]
min_max_scaler = preprocessing.MinMaxScaler()
print(min_max_scaler)
# MinMaxScaler(copy=True, feature_range=(0, 1))
print('============================')
x_minmax = min_max_scaler.fit_transform(x)
print(x_minmax)
#就是打印的数组
# [[1.         0.         1.         1.        ]
#  [0.66666667 0.33333333 0.6        0.238     ]
#  [0.         0.66666667 0.4        0.        ]
#  [0.33333333 1.         0.         0.752     ]]

print('============================')

max_abs_scaler = preprocessing.MaxAbsScaler()
x_train_maxsbs = max_abs_scaler.fit_transform(x)
print(x_train_maxsbs)
# [[ 1.         -0.5         0.66666667  1.        ]
#  [ 0.66666667  0.          0.          0.37846656]
#  [ 0.          0.5        -0.33333333  0.18433931]
#  [ 0.33333333  1.         -1.          0.79771615]]
print('============================')

#正态化数据
transformer = StandardScaler().fit(x)
x_train_standardSca = transformer.fit_transform(x)
print(x_train_standardSca)
# [[ 1.34164079 -1.34164079  1.38675049  1.26405295]
#  [ 0.4472136  -0.4472136   0.2773501  -0.65277958]
#  [-1.34164079  0.4472136  -0.2773501  -1.25147531]
#  [-0.4472136   1.34164079 -1.38675049  0.64020194]]

print(math.log10(1/8/pow(2,0.5))/2)
