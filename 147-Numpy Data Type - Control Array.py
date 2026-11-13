#----------------------------------------------
#---- Numpy => Data Type And Control Array ----
#----------------------------------------------
# https://numpy.org/doc/stable/user/basics.types.html
# https://docs.scipy.org/doc/numpy/reference/arrays.scalars.html
#----------------------------------------------
# '?' boolean
# 'b' (signed) byte
# 'B' unsigned byte
# 'i' (signed) integer
# 'u' unsigned integer
# 'f' floating-point
# 'c' complex floating-point
# 'm' timedelta
# 'M' datetime
# 'O' (Python) objects
# 'S', 'a' zero-terminated bytes (not recommended)
# 'U' Unicode string
# 'V' raw data (void)
#----------------------------------------------

import numpy as np

# Show Array Data Type

my_array = np.array([1, 2, 3, 4, 5])
my_array2 = np.array([1.5 , 20.15, 3.601])
my_array3 = np.array(["Hussien", "A", "Ahmed"])

print(my_array.dtype) # int64
print(my_array2.dtype) # float64
print(my_array3.dtype) # <U7

print("#" * 50)

# Create Array With Specific Data Type

my_array4 = np.array([1, 2, 3, 4, 5],dtype=float) # float Or 'float' Or 'f'
my_array5 = np.array([1.5 , 20.15, 3.601], dtype=int) # int Or 'int' Or 'i'
#my_array6 = np.array(["Hussien", "A", "Ahmed"], dtype=int) # ValueError

print(my_array4.dtype)
print(my_array5.dtype)
# print(my_array6.dtype)

print("#" * 50)

# Change Data Type Of Existing Array

my_array7 = np.array([0, 1, 2, 3, 0, 4])
print(my_array7.dtype) # int64
print(my_array7)

print("#" * 50)

my_array7 = my_array7.astype('float') 
print(my_array7.dtype) # float64
print(my_array7)

print("#" * 50)

my_array7 = my_array7.astype('bool')
print(my_array7.dtype) # bool
print(my_array7)

print("#" * 50)

# Test Capacity

my_array8 = np.array([100, 200, 300, 400, 500], dtype='f')
print(my_array8.dtype) 
print(my_array8[0].itemsize) # 4 Bytes

my_array8 = my_array8.astype('float') # change to float64
print(my_array8.dtype)
print(my_array8[0].itemsize) # 8 Bytes