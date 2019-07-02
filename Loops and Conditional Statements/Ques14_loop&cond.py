print("Question 14")
print("Enter String")
a=input()
l=len(a)
alp=0
dig=0
print(l)
for n in range(l):
    b=a[n]
    if b.isalpha()==True:
        alp+=1
    if b.isdigit()==True:
        dig+=1
print("Letters",alp)
print("Digits",dig)
