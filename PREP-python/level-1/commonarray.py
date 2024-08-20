#numpy

import numpy as np
input1=input().split()
input2=input().split()
array1=np.array(input1,int)
array2=np.array(input2,int)
print(np.intersect1d(array1,array2))