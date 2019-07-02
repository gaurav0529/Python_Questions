print("Question 13")
print("Enter 4 digit Numbers seprated by Comma")
n=input()
a=n.split(",")
print(a)
l=len(a)
print("Length",l)
for n in range(l):
    d=int(a[n])
    if d%5==0:
        print(d)
