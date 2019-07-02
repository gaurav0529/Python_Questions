#Question 3
ls=[]
i=int(input("Enter No of Elenents in List:"))
for n in range(i):
    ls.append(int(input("Enter Integer Number:")))
print(ls)
ls.sort(reverse=True)
print(ls[0])
