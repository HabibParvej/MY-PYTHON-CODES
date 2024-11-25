# APPEND Function
l=[10,20,30,40,30,31,20]
l.append(50)
print('APPEND:',l)


# Extend function
l.extend([60,70])
print('Extend:',l)

#Insert function
l.insert(2,110)
print('Insert:',l)

#Index function
print('Index:',l.index(110))

# Count function
print('Count:',l.count(20))

# sort function
l.sort()
print('Sort:',l)
print('Reverse Sorting:',l.reverse())
print(l)
print('Reverse Sorting:',l.sort(reverse=True))
print(l)

#Deletion in a list
print('Before Poped:',l)
l.pop()
print('After Poped:',l)

# Remove Function
print('Before Removed:',l)
l.remove(30)
print('After Removed:',l)

# Del function
print('Before Deleted:',l)
del l[1]
print('After Deleted:',l)

# Matrix
l1=[0 for i in range (5)]
print(l1)
#2D Matrix
l2=[[0 for i in range(5)] for j in range(5)]
print(l2)