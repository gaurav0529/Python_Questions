
# Question 26
st=""
for r in range(7):
    for c in range(1,6):
        if ((r==0 and c>1)or(r==1 and c==1)or(r==2 and c==1)or(r==3 and(c>1 and c<5))or(r==4 and c==5)or(r==5 and c==5)or(r==6 and c<5)):
            st+="*"
        else:
            st+=" "
    st+="\n"
print(st)



st=""
for r in range(15):
    for c in range(1,18):
        if ((r==0 or r==1 or r==2 or r==6 or r==7 or r==8 or r==12 or r==13 or r==14)or((r==3 or r==4 or r==5)and c<5)or((r==9 or r==10 or r==11)and c>11)):
            st+="o"
        else:
            st+=" "
    st+="\n"
print(st)
