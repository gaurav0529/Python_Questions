# Question 36
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
if a==b and a==c:
    print("Equilateral Triangle")
elif a==b or a==c or b==c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
