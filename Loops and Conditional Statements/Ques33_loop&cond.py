#Question 33
print("Enter first 3 Latters of month as :- Jan,Feb,Mar......")
m=input("Enter Month Name: ")
if m=='Jan' or m=='Mar' or m=='May' or m=='Jul' or m=='Sep' or m=='Nov' :
    print("31 Days")
elif m=='Feb':
    print("28/29 days")
elif m=='Apr' or m=='Jun'or m=='Aug' or m=='Oct' or m=='Dec':
    print('30 days')
else:
    print("Enter Valid Name")
