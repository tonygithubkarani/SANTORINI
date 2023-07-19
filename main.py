from collections import namedtuple
a=namedtuple('courses','name,technology')
s=a('Tony','python')
print(s)
from collections import deque
a=['e','d','r','y','k']
d=deque(a)
d.append('python')
print(d)

from collections import ChainMap
a={1:"Edureka",2:"Tony"}
b={3:"Book",4:"Bottle"}
s=ChainMap(a,b)
print(s)

from collections import Counter
a={1,1,4,2,3,3,2,4,5,5,6,6,6,7,7,8,8,9,9,9,9}
b=Counter(a)
sub={2:1,6:1}
print(b.subtract())

from collections import OrderedDict
d=OrderedDict()
d[1]='o'
d[2]='k'
print(d)
from collections import defaultdict
d=defaultdict(int)
d[1]='python'
d[2]='edureka'
print(d[3])

import sys
print(sys.path)

#Arrays
import array
a=array.array("i",[1,2,3,4,5,6,7,8])
a.pop(0)
print("array a=",a[0:3])

import Sally as S
addition=S.add(2,2)
print(addition)

import numpy as np
ar1= np.array([1,2,3,4])
print(ar1)