#Lambda function
s=lambda x:x*x
print(s(3))

#filter
my_list=[2,3,4,5,6,7,8]
List = list(filter(lambda a:a/3==2,my_list))
print(List)
#map
my_list=[2,3,4,5,6,7,8]
List = list(map(lambda a:a/3!=2,my_list))
print(List)
#Reduce
from functools import reduce
a=reduce(lambda a,b:a+b,[2,3,4,5,6,7,8])
print(a)
#Algebraic expressions
s=lambda a:a*a
print(s(4))

c = filter(lambda x:(x>=4),map(lambda x:x+x,[2,3,4,5,6,7,8,9]))
print(tuple(c))

def new(a,b):
    return a*b
x=map(new,[1,2,3,4,5],[1,2,3,4,5])
print(x)
print(list(x))

def new1(i):
    if i >=3:
        return i
j=filter(new1,[1,2,3,4,5,6,7])
print(j)
print(tuple(j))

from functools import reduce
def a(x,y):
    return x+y
s=reduce(a,[1,2,3,4,5,6,7,8,9])
print(s)