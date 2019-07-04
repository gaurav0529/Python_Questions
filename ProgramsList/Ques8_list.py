#question 8
li=[]
print("enter no of elements")
l=int(input())
for n in range(l):
    li.append(input())
print(li)
if len(li)==0:
    print("list is empty")
else:
    print("list is not empty")
