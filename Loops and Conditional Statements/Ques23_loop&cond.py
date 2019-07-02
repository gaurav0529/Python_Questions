# Question 23
st=""
for r in range(7):
    for c in range(7):
        if (((c==1 or c==5)and(r!=0 and r!=6)) or((r==0 or r==6) and(c>1 and c<5))):
            st+="*"
        else:
            st+=" "
    st+="\n"
print(st)
