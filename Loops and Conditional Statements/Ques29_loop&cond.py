
# Question 29
st=""
for r in range(7):
    for c in range(5):
        if (((c==0 or c==4)and(r!=2 and r!=3 and r!=4))or((r==2 or r==4)and(c==1 or c==3))or(r==3 and c==2)) :
            st+="*"
        else:
            st+=" "
    st+="\n"
print(st)


