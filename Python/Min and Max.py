import numpy as np

N, M = map(int, input().split())

arr = np.array([input().split() for i in range(N)],int)

#Get the min over axis 1
Min = np.min(arr, axis=1)

#Get the maximum of the minimum in axis 0
Max = np.max(Min, axis=0)

print(Max)
