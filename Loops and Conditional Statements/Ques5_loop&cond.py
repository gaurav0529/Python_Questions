print("Question 5")
print("Enter String")
a=input()
l=len(a)
r=""
for i in range(l-1,-1,-1):
    r=a[i]
    print(r,end="")
