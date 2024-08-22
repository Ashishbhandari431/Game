# import numpy as np
# a=np.array([[10,20],
#             [30,40]])
# b=np.array([[2,3],
#             [5,6]])
#print(a+b)
# print(a-b)
# print(a*b)
# print(a**b)
# print(a/b)
# print(a//b)
#print(a@b) matrix multiplications
#print(a%b)

#SORTING:-
import numpy as np
a=np.array([[10,20,12,11,1],
            [34,44,32,21,2]])
#b=np.sort(a)[::-1]
#print(b)
#c=np.argsort(a)
#print(c)
b=np.sort(a, axis=0)
print(b)
c=np.argsort(a, axis=0)
print(c)
a.sort()
print(a)
