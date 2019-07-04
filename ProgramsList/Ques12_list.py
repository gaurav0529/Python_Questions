ls=['red','green','white','black','pink','yellow']
print(ls)
n=int(input("how much you want to remove "))
for i in range(n):
    ls.remove(ls[int(input("Enter Pos "))-i])
print(ls)


