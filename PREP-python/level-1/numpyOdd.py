
import numpy as np
input_list = input().split()
arr = np.array(input_list,int)
print(arr[arr % 2 == 1])
