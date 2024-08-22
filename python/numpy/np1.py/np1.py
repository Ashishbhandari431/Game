import numpy as np
#arr = np.array([1,2,3])
# print(arr[0])
# print(arr[1])
b=np.array([[10,30,40],[23,67,78],[56,89,99]])
# print(b[1,2])
# print(b[1,1])
# print(b[2,2])
# print(b[0,1])
#print(b.ndim)

#slicing in array:-(single dimensional)
# b=np.array([12,23,45,36,67])
# print(b[2:5])
# print(b[0:2])
# print(b[0:5:2])
# print(b[::-1]) reverse print

#slicing in multidimensional array:-
#print(b[1:3,1:3])
#print(b[0:2,0:2])
#print(b[0:3,1:3])
print(b.ndim)
a=np.array([12,23,34,45,56,67,78,89])
print(a.ndim)
c=np.array([[[12,23],[34,45],[56,67]]])
print(c.ndim)
d=np.array(12)
print(d.ndim)