import numpy as np
arr=np.array(17)
brr=np.array([1,2,3,4,5])
crr=np.array([[1,2,3,4,5]])
drr=np.array([[[1,2,3,4,5]]])
print(arr)
print(type(arr))
print(arr.ndim) #to obatain how many dimension
print(arr.shape)
print(arr.size)
print(arr.dtype)
print(brr)
print(type(brr))
print(brr.ndim)
print(brr.shape)
print(brr.size)
print(brr.dtype)
print(crr)
print(type(crr))
print(crr.ndim)
print(crr.ndim)
print(crr.shape)
print(crr.size)
print(crr.dtype)
print(drr)
print(type(drr))
print(drr.ndim)

#creat a 3D array with 2D array both contains 2 array value of [1,2,3,4,5,6] 

import numpy as np
arr1 = np.array([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]])
arr2 = np.array([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]])
array_3d = np.array([arr1, arr2])
print(array_3d)
print(array_3d.ndim)