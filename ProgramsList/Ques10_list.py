st=input("Enter string: ")
wd=st.split(" ")
print(wd)
n=int(input("Enter no to get more than that words "))
ls=[]
for i in wd:
    if len(i)>n:
        ls.append(i)
print(ls)



