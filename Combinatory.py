def fact(n):
    f=1
    while(n>0):
        f=f*n
        n-=1
    return f
def main():
    n=int(input("Enter the value of n:"))
    r=int(input("Enter the value of r:"))
    c=fact(n)/(fact(n-r)*fact(r))
    print(c)  
    # print(fact(n))  
if __name__ =='__main__':
    main()