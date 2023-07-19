#Try and Except error
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print(result)
    my_list = [1,2,3]
    i = int(input("Enter index: "))
    print(my_list[i])
except ZeroDivisionError:
    print("Denominator cannot be 0.Please try again.")
except IndexError:
    print("Index cannot be greater than size of list.")

print("program ends")

#finally
try:
    print(1/0)
except:
    print("Wrong denominator")
finally:
    print("Always printed")

try:
    numerator= int(input("Enter numerator: "))
    denominator= int(input("Enter denominator:"))
    result = numerator/denominator
    print(result)
except ZeroDivisionError:
    print("Hold on")
else:
    try:
        list = [1,2,3,4]
        i = int(input("Enter index: "))
        print(i)
    except IndexError:
        print("Index cannot be greater than list")
print("program ends")
