
# Question 27
st=""
for r in range(7):
    for c in range(5):
        if ((r==0)or(c==2)) :
            st+="* "
        else:
            st+="  "
    st+="\n"
print(st)

