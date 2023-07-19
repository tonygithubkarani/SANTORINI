#Numpy
import numpy as np
a =np.array([1,2,3])
print(a)
print(a[1])

import sys
import numpy as np
import time
b =range(1000)
print(sys.getsizeof(5)*len(b))

c = np.arange(1000)
print(c.size*c.itemsize)

size = 10000
l1 = range(size)
l2= range(size)
A1=np.arange(size)
A2=np.arange(size)

start = time.time()
result= [(x+y) for x,y in zip(l1,l2)]
print(result)
print("python list took:",(time.time()-start)*1000)

start =time.time()
result = A1+A2
print(result)
print("python nunmpy took:",(time.time()-start)*1000)

a = np.array([[1,2],[3,4],[5,6]],dtype=complex)
print(a)

import numpy as np
print(np.ones((4,3)))

import numpy as np
print(np.char.add(["Hello","Hi"],["ABZ","Tony"]))

print(np.char.center("hello",28,fillchar="-"))

print(np.char.join([":",'.'],["dmy","jmd"]))

#Part two
#Array manipulation-changing shape
import numpy as np
a= np.arange(9)
print(a)
b= a.reshape(3,3)
print(b)

print(b.flatten(order = "F"))

a=np.arange(12).reshape(4,3)
print(np.transpose(a))

b= np.arange(8).reshape(2,2,2)
print(np.swapaxes(b,1,2))

#Numpy arithetic operations
a= np.arange(9).reshape(3,3)
print(a)

b=np.array([10,11,12])
print(np.multiply(a,b))

#Slicing
a = np.arange(20)
print(a[4])

s = slice(2,9,2)
print(a[s])

#Iterating over Array
a = np.arange(0,45,5)
a =a.reshape(3,3)
#Iteration order(c-style and f-style
for x in np.nditer(a,order = "F"):
    print(x)

#JOINING ARRAYS
a = np.array([[1,2],[3,4]])
print("a")
b = np.array([[5,6],[7,8]])
print(b)
print(np.concatenate((a,b)) )
print(np.concatenate((a,b),axis = 1))

#Splitting the Array
a = np.arange(9)
print(a)
print(np.split(a,[4,7]))

#RESIZING THE ARRAY
A= np.array([[1,2,3],[4,5,6]])
print(A)
print(a.shape)
b = np.resize(a,(2,3))
print(b)
print(b.shape)

#HISTOGRAM
from matplotlib import pyplot as plt
a= np.array([20,87,4,40,53,74,56,51,11,20,40,15,79,25,27])
plt.hist(a,bins=[0,20,40,60,80,100])
plt.title("HISTOGRAM")

#Other useful functions in numpy
#linespace function
a = np.linspace(1,3,10)
print(a)

#sum and axis
a = np.array([(1,2,3),(3,4,5)])
print(a.sum(axis=0))
#squareroot and standard deviations
a = np.array([(1,2,3),(3,4,5)])
print(np.sqrt(a))
print(np.std(a))
#ravel
a = np.array([(1,2,3),(3,4,5)])
print(a.ravel())
print(np.log10(a))

#numpy practise example
import matplotlib.pyplot as plt
x = np.arange(0,3*np.pi,0.1)
y = np.sin(x)
plt.plot(x,y)

#create 2-dimensional array ,and let 1 and 0 be placed alternatively across the diagonals
z =np.zeros((6,6),dtype=int)
z[1::2,::2]=1
z[::2,1::2]=1
print(z)