"""
n = int(input("Enter a number to Check "))
#121
s = n
a = 0
while(s!=0):
    r = s % 10
    a = a*10 + r
    s = s//10

if a == n:
    print("Pallindrome")
else:
    print("Not pallindrome")
"""


def pall(s):
    a = 0
    while(s!=0):
        r = s % 10
        a = a * 10 + r
        s = s//10
    return a
n = int(input("Enter a number to check "))
a = pall(n)
if a == n:
    print(" Pallinrome ")
else:
    print(" not Pallindrome ")