d=dict()
d[1]='puja'
d[2]='Ram'
d[3]='Raghav'
d['sonam']=5
print(d) # {1: 'puja', 2: 'Ram', 3: 'Raghav', 'sonam': 5}

r=[1,2,3,4,5]
n=['a','b','c','d','e','f']
d2=dict(zip(r,n))
print(d2) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print(d2[4]) # d
for i in d2.keys():
    print(i) # 1 2 3 4 5
for i in d2.values():
    print(i) 
for i in d2.items():
    print(i) 