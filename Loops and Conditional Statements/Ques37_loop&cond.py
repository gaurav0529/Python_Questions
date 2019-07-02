#Question 37
print("Enter first 3 Latters of month as :- Jan,Feb,Mar......")
m=input("Enter Month Name: ")
if m=='Mar' or m=='Apr' or m=='May':
    print("Summer or Pre-Monsoon")
elif m=='Jun' or m=='Jul' or m=='Aug' or m=='Sep':
    print("Monsoon or Rainy")
elif m=='Oct' or m=='Nov':
    print('Post-Monsoon or Autumn')
elif m=='Dec' or m=='Jan' or m=='Feb':
    print('Winter')
else:
    print("Enter Properly")
if m=='Jan' or m=='Mar' or m=='May' or m=='Jul' or m=='Sep' or m=='Nov' :
    print("31 Days")
elif m=='Feb':
    print("28/29 days")
elif m=='Apr' or m=='Jun'or m=='Aug' or m=='Oct' or m=='Dec':
    print('30 days')
else:
    print("Enter Valid Name")
