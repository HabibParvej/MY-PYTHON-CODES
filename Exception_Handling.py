# def find(st,ind):
#     print(st[ind])

# st=input("Enter your String")
# try:
#     find(st,5)
# except IndexError:
#     print("Index Error Caught:")
# print("End of the program")


a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
def find(st,ind):
    
    print(st[ind])

st=input("Enter your String:")
try:
    print(find(st,5))
    div=a/b
    print(div)
except IndexError:
    print("Index Error Caught:")
except ZeroDivisionError:
    print("ZeroDivisionError Caught:")
# except (bad,fault):
#     print("Exception Caught:")
print("End of the program::")


#OR

# except (IndexError,ZeroDivisionError):
#     print("Index Error or ZeroDivisionError Caught:")

