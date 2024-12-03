#same as list but immutable
t=(12,13)
print(t[0]) #12
print(t[1])   #13
print(len(t))   #2



#Set (mutable,and we can intersect and union also)
s1={1,2,3,4}
print(s1)  #{1, 2, 3, 4}

s2={1,2,3,4,4,5,5,6,6}
print(s2)  #{1, 2, 3, 4, 5,6}
#set is unordered collection of unique elements
print(s1.intersection(s2)) #{1,2,3,4}
print(s1.union(s2)) #{1, 2, 3, 4,5,6}
s1.add(7)
print(s1)  #{1, 2, 3, 4, 7}
s2.update(s2)
print(s2)  #{1, 2, 3, 4, 5,6}


a=10
b=15
s=a+b
print(s)  #25


# s=ab+ syntax errror
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
avg=a+b/2
print(avg) #logical error






