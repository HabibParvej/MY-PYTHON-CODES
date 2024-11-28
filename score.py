score = {'pl1':100,'pl2':80,'pl3':72,'pl4':85,'pl5':30,'pl6':102}
#print(sum(score.values()))
#sum=0
max=0
for i in score.values():
    #sum+=i
    if i>max:
        max=i
print(max)     
for i in score.keys():
    if score[i]==max:
        max=i

#print(sum)
print(max)

# Method 2

for i in score.keys():
    if max not in score.keys():
        max=i
print(max)


