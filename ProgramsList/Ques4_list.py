
#Question 4
ls=[]
i=int(input("Enter No of Elenents in List:"))
for n in range(i):
    ls.append(int(input("Enter Integer Number:")))
print(ls)
ls.sort()
print(ls[0])
