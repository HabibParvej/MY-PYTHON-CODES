d = {"sonam":1,
     "Ram":2,
     3:[10,20,30],
     4:{5:"a",6:"b"}
     }

print(d["sonam"])
print(d[3])
print(d[4])
print(d[4][5])
print(d[4][6])
print(d.items())
print(d.keys())
print(d.values())
# if we want to update
d[3]='abhay'
print(d[3]) #updated value
# if we want to add new key value pair
d[5]='puja'
print(d[5]) #new value

# if we want to change the nested dictionaries value
d[4][5]='sajid'
print(d[4][5]) #updated value