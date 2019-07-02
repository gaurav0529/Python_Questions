#Question 5
ls=['abc','xyz','aba','1221']
count=0
for n in range(4):
    if len(ls[n])>=2:
        l=ls[n]
        if l[0]==l[len(l)-1]:
            count+=1
print(count)
