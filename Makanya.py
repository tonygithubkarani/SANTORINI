#Decorators
def func1(name):
    return f"hello {name}"
def func2(name):
    return f"{name},how are you doing?"
def func3(func4):
    return func4("Dear learner")
print(func3(func1))
print(func3(func2))

def outer():
    x=3
    def inner():
        y=3
        result=x+y
        return result
    return inner()

a=outer()
print(a)

#Decoration
def function1():
    print ("hi i am function 1")
def function2(func):
    print ("hi i am function 2 now i wil call function1")
    func()
function2(function1)
def outer(expr):
    def str_upper(func):
      def inner():
          str1 = func() + expr
          return str1.upper()
      return inner
    return str_upper
@outer(" Tony")
def print_str():
    return "good morning"
print(print_str())
def div_decorator(func):
    def inner(*args):
        list1 = args[1:]
        for i in list1:
            if i==0:
                return "Give proper input"
        return func(*args)
    return inner
@div_decorator
def div(a,b):
    return a/b
@div_decorator
def div1(a,b,c):
    return a/b/c
print(div(10,0))
print(div1(10,2,2))

def greet(name):
    print("Hello",name)
    print("How do you do?")
greet("Tony")

def add_numbers(n1,n2):
    result = n1+n2
    return result


a= add_numbers(10,2)
print("The sum is",a)


def f1(func):
    def inner(*args, **kwargs):
        print("Started")
        val= func(*args, **kwargs)
        print("Ended")
        return val
    return inner
@f1
def f(a=1,b=2):
    print(a,b)
f()
@f1
def add (x,y):
    return x+y
print(add(4,5))
@f1
def div(a,b,c):
    return a/b/c
print(div(10,2,2))
