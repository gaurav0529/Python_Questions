print("2. Write a Python program to convert temperatures to and from celsius, fahrenheit.")
print("Choose (1 or 2) to convert into:\n1. Celsius\n2. Fahrenheit")
a=int(input())
if a==1:
    print("Enter temp in Celsius")
    c=int(input())
    f=((9*c)/5)+32
    print("Degree in Fahrenheit",f)
else:
    print("Enter temp in Fahrenheit")
    f=int(input())
    c= ((f-32)/9)*5 
    print("Degree in Celsius ",c)
