# Question 22
st=""
for r in range(7):
    for c in range(7):
        if ((c==1 or c==5) or(r==2 and(c==2 or c==4))or (r==3 and c==3)):
            st+="* "
        else:
            st+="  "
    st+="\n"
print(st)
