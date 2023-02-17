
import numpy as np
import time

tic=time.process_time()
a=np.arange(0,50)
b=np.arange(0,50)
sum=0
for i in range(50):
    sum=(a[i]*b[i])+sum
print('inner product: ',sum)



print('----------------------------------------------------')


toc=time.process_time()

print('computational time for non-vector method:',toc-tic)

print('----------------------------------------------------')




tic_2=time.process_time()
c=np.inner(a,b)
print('inner product(vectorisation method):',c)
toc_2=time.process_time()
print('----------------------------------------------------')

print('computational time for vector method:',toc_2-tic_2)

print('----------------------------------------------------')

def outer_product(a, b):
    m = len(a)
    n = len(b)
    result = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(a[i] * b[j])
        result.append(row)
    return result

e=outer_product(a,b)
print('outer product',e)



print('----------------------------------------------------')



d=np.outer(a,b)

print('outer product (vectorization method):',d)






