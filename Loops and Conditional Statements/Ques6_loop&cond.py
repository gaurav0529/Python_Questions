print("Question 6")
print("How much No. do you want to enterd")
l=int(input())
ls=[]
print("Enter No :-")
for n in range(l):
    ls.append(int(input()))
print(ls)
c=0
d=0

for n in range(l):
    if ls[n]%2==0:
        c+=1
    else:
        d+=1
print("No. of Even No. :-",c)
print("No. of Odd No. :-",d)
