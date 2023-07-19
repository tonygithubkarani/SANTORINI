#SCIPY
#Basic functions
from scipy import cluster
help(cluster)
import numpy
numpy.info(cluster)

#Special functions
#Exponential and Trigonometric functions
from scipy import special
a= special.exp10(2)
print(a)

from scipy import special
a = special.sindg(90)
print(a)

#Intergration functions :not coverd well

#fourier transformations
from scipy.fftpack import fft,ifft
import numpy as np
x =np.array([1,2,3,4])
y = fft(x)
print(y)

#Linear algebra-not covered well

#Interpolation functions
f