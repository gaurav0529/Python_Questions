#Question 31
n=float(input("Age in Human Year: "))
if n<=2:
    a=n*10.5
else:
    a=(2*10.5)+((n-2)*4)
print("Age in Dog's Year: ",a)
