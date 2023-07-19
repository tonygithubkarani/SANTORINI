def add(a,b):
    return a+b
def divide(a,b):
    return a/b
def prod(a,b):
    return a*b
def sub(a,b):
    return a-b

#FILE HANDLING
x=open("demo.txt","a")
x.write("We love Edureka")
x.close()

import os
os.path.exists("demo.txt")
os.remove("demo.txt")

