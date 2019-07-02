# Question 21
st=""
for r in range(7):
    for c in range(7):
        if ((c==1)or(r==6 and (c>1 and c<6))) :
            st+="*"
        else:
            st+=" "
    st+="\n"
print(st)
