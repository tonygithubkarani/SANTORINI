my_dict={"Dave":'001',"Tony":'002',"Carol":'003'}
del my_dict['Dave']
print(my_dict)

x=11
print(not(x>5 and x>10))

list1=[10,20,30]
list2= [10,20,30]
x=list1
print (10 in list1)

#Patterns in python
#Single square  pattern
n=int(input("Enter number of rows:"))
for i in range (n):
     for j in range(i,n):
         print(" ",end="")
     for j in range(i+1):
         print("*",end="")
     print()

string=input('Enter the string:')
length =len(string)
for i in range(length):
    for j in range(i+1):
        print(string[j],end="")
    print()

n= int(input("Enter the number of rows;"))
for i in range(n):
    for j in range(n):
      if (j==0 or j==n-1):
        print("*",end=" ")
      else:
          print(" ",end=" ")
    print()

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()
n=5
for i in range(n):
    for j in range(n-1):
        print(" ",end="")
    for j in range(i,n-1):
        print("*",end="")
    for j in range(i,n):
        print("*",end="")
    print()
