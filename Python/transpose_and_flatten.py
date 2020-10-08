import numpy as np

a = input().split(' ')
b = tuple(map(int, a))

c = []
for i in range(b[0]):
    c.append(input().split(' '))
    
c = np.array(c, int)
#Print out the transpose
print (np.transpose(c))
#Flatten the array
print (c.flatten())
