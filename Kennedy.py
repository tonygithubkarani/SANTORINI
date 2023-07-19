#Generators
def func(a):
    yield a
a = [1,2,3]
b = func(a)
print(next(b))

def my_gen():
    n=1
    print("This is printed first")
    yield n
    n=n+1
    print("This is printed second")
    yield n
a=my_gen()
for i in a:
    print(i)

def new(dict):
    for x,y in dict.items():
        yield x,y
a = {1:"Hi",2:"Welcome"}
b = new(a)
print(next(b))
print(next(b))

#Generator expressions
a = range(6)
print("gen exp",end=":")
q = [x+2 for x in a]
print (min(q))
a = range(6)
print("list comp",end=":")
q = [x+2 for x in a]
print(q)

#Finobacci series
def fib():
    f,s = 0,1
    while True:
        yield f
        f,s=s,f+s
for x in fib():
    if x>50:
        break
    print(x,end=" ")

#Number stream
a=range(1,100,2)
b=(x for x in a)
for x in b:
    print(x)