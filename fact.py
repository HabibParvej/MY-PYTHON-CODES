#i = 1\ 
"""
def fact(x) :
    if x == 0 or x == 1 :
        return 1
factor = 1
  while(x > 1) :
    factor = factor * x
    factor = factor - 1
return factor
x = 5
print("factorial is ",factor)
 
 """
 
 
 
 
def fact(x):
    if x == 0 or x == 1:
        return 1
    factor = 1
    while x > 1:
        factor = factor * x
        x = x - 1
    return factor

x = int(input("Enter a number = "))

print("factorial is =", fact(x))
