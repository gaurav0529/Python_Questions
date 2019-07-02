result=""
for r in range(7):
    for c in range(7):
        if (((c==1 or c==5) and r!=0)or((r==0 or r==3) and (c>1 and c<5))):
            result+="*"
        else:
            result+=" "
    result+="\n"
print(result)



