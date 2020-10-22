import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr_ = numpy.array(arr, float)
    return arr_[::-1]


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
