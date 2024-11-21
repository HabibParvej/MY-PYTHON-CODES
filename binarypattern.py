
#s=0
for i in range (7,0,-2):
    for k in range (i,7):
        print(' ', end='')
    for j in range (i,0,-1):
        if(j%2==0):j=0
        else:j=1
        print(j,end=' ')  
    print()
    #s+=1  