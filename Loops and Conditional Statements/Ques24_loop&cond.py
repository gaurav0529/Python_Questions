# Question 24
st=""
for r in range(7):
    for c in range(7):
        if ((c==1)or((r==0 or r==3)and(c>1 and c<5))or((r==1 or r==2)and c==5)):
            st+="*"
        else:
            st+=" "
    st+="\n"
print(st)



