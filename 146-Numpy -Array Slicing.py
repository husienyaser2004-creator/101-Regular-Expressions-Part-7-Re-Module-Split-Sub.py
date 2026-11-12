#-------------------------------------
#-numpy array slicing
#-------------------------------------

import numpy as np

# slicing => [start:stop:steps] Not include End

a = np.array(["A", "B", "C", "D", "E", "F"])

print(a.ndim) # 1
print(a[1])
print(a[1:4]) # ['B' 'C' 'D']
print(a[:4]) # ['A' 'B' 'C' 'D']
print(a[2:5]) # ['C' 'D' 'E']
print(a[2:]) # ['C' 'D' 'E' 'F']
print(a[::2]) # ['A' 'C' 'E']

print("#" * 50)


b = np.array([["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], ["J", "K", "L"]])

print(b.ndim) # 2
print(b[1]) # ['D' 'E' 'F']

print("#" * 50)

print(b[2:, :2])
print(b[2:, 2:3]) 