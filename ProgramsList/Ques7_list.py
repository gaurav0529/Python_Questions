li=[]
print("enter no of elements")
l=int(input())
for n in range(l):
    li.append(input())
print(li)
fl=[]
for n in li:
    if n not in fl:
        fl.append(n)
print(fl)
