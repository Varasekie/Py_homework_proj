import numpy as np
arr = np.array([[1,-2,0],[-2,2,-2],[0,-2,3]])
c = np.linalg.eig(arr)[0]
d = np.linalg.eig(arr)[1]
print(c,d)

