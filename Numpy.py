import numpy as np
a = np.array([(1,2,3),(4,5,6)])
print(a)

import numpy as np
import time
import sys
s = range(1000)
print(sys.getsizeof(5)*len(s))
D = np.arange(1000)
print(D.size*D.itemsize)

import numpy as np
import time
import sys
size=1000000
l1 = range(size)
l2=range(size)

A1= np.arange(size)
A2= np.arange(size)

start=time.time()
result = [(x,y) for x,y in zip(l1,l2)]
print((time.time()-start)*1000)

start =time.time()
result = A1+A2
print((time.time()-start)*1000)

#Numpy operations
import numpy as np
a = np.array([(1,2,3),(3,4,5)])
print(a.ndim)
print(a.itemsize)
print(a.dtype)
print(a.shape)
import numpy as np
a = np.array([(1,2,3,2),(3,4,5,6)])
print(a[0:1,3])
print(a[0,2])

import numpy as np
a = np.linspace(1,2,3)
print(a)

#Maximu,minimum,sum
import numpy as np
a = np.array([1,2,3])
print(a.max())
print(a.sum())

#Axis
#axis 1= rows
#axis 0=columns
import numpy as np
a = np.array([(1,2,3),(3,4,5)])
print(a.sum(axis = 1))

#Numpy special functions
#cosine
#sine
import numpy as np
import matplotlib.pyplot as plt
x =np.arange(0,3*np.pi,0.1)
y= np.sin(x)
plt.plot(x,y)
plt.show()
import numpy as np
import matplotlib.pyplot as plt
a= np.array([1,2,3])
print(np.exp(a))

import numpy as np
a = np.array([1,2,3])
print(a)



