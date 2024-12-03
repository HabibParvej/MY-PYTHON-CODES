# Creating a custom exception/user defined exception
class Sreya(Exception):
    pass
a=int(input("Enter 1 if present else 2::"))
try:
    #print("this is try block")
    if a%2==0:
        raise Sreya

except Sreya:  
    print("She is not in the classroom:::")

# finally:
#     print("This is finally block")
#     print("Present:")
else:
    print("She is in the classroom:::")

finally:
    print("This is finally block")


