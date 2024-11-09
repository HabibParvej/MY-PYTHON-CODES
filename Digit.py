n=4347638
sum=0
r=1

while(n!=0):
    dig=n%10
    n=n//10

    if(dig%2==0):
        dig+=2
    
    else:
        dig+=1

    if dig==10 or dig==0:
        dig=0


    sum=sum+dig*r
    r=r*10
print(sum)