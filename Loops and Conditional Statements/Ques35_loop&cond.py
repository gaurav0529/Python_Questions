# Question 35
a=input()
l=len(a)
dig=0
for n in range(l):
    b=a[n]
    if b.isdigit()==True:
        dig+=1
if dig==l:
    print("The string is an integer.")
else:
    print("The string is not an integer.")
