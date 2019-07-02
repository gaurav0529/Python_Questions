n=int(input("Enter Number of Integer Numbers : "))
add=0
count=0
for i in range(n):
    a=int(input())
    if a==0:
        break
    add+=a
    count+=1
print("Sum :",add)

print("Avg :",(add/count))
