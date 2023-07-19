#Classes and Objects
#Inheritance
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks = marks
    def check_pass_fail(self):
        if self.marks>=40:
            return True
        else:
            return False
student1=student("Tony",85)
student2=student("Silas",30)
print(student1.check_pass_fail())

class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def add(salf,number):
        real = salf.real + number.real
        imag = salf.imag + number.imag
        result=complex(real ,imag)
        return result
n1=complex(5,6)
n2=complex(-4,2)
result = n1.add(n2)
print("real=",result.real)
print("imag=",result.imag)

#Inheritance
class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def view(self):
        print(self.name,self.age)
class child(parent):
    def __init__(self,name,age):
        parent.__init__(self,name,age)
        self.lastname="Edureka"
    def view(self):
        print(self.name,self.age,self.lastname)
ob=child("Tony",19)
ob.view()


def add(a,b):
    return a+b
def divide(a,b):
    return a/b
def prod(a,b):
    return a*b
def sub(a,b):
    return a-b


