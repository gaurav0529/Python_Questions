#Question 41
y=int(input("Input a year:"))
m=int(input("Input a Month [1-12]:"))
d=int(input("Input a day [1-31]:"))
if m==2:
    if y%4==0:
        for n in range(1,30):
            if d>29:
                print("Enter Valid Date")
                break
            elif d==29:
                m+=1
                print("%s-%s-1"%(y,m))
                break
            else:
                n==d
                d+=1
                print("%s-%s-%s"%(y,m,d))
                break
    else:
        for n in range(1,29):
            if d>28:
                print("Enter Valid Date")
                break
            if d==28:
                m+=1
                print("%s-%s-1"%(y,m))
            else:
                n==d
                d+=1
                print("%s-%s-%s"%(y,m,d))
                break
elif m%2==0:
    for n in range(1,31):
            if d==30:
                m+=1
                print("%s-%s-1"%(y,m))
                break
            else:
                n==d
                d+=1
                print("%s-%s-%s"%(y,m,d))
                break
else:
    for n in range(1,32):
            if d==31:
                m+=1
                print("%s-%s-1"%(y,m))
                break
            else:
                n==d
                d+=1
                print("%s-%s-%s"%(y,m,d))
                break
