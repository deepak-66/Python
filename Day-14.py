#1. Best seller Tag Display
'''
ps=int(input("Enter the Product Sales : "))
if ps<0:
    print("You entered negative values")
'''
#2. Zepto Rain Delivery Charges
'''
rain=input("Enter True/False for Rain Or Not : ")
print(rain)
if rain == "True":
    print("Extra Rain Charges Applied")
'''
#4 Delivery Caharge Calculation
'''
bill=int(input("Enter the Order Value : "))
if bill<=99:
    print(f'Final Bill Amount : {bill+30}')
    print('Add more then 99 to get free delivery charges 30/-')
else:
    print(f'Final Bill Amount : {bill}')
    print('you have free delivery charges')
'''

#5 Weekend Palnner Based On Budget
'''
Budget=int(input("Entre Your Budget : "))
if Budget>10000:
    print("You can go to Trip")
elif Budget>5000:
    print("Resort Stay")
elif Budget>3000:
    print("Movie and Dinner")
elif Budget>1000:
    print("Cafe and Shopping")
elif Budget>500:
    print("street food and Park Visit")
else:
    print("Stay At Home Please!!! you Poor guy")
'''

#Repetition Statements(Loops) --> Loops Help us in automating repetitive.
#task--> for,while

#for loop --> It is used mainly to iterate whithiin in list,strings,renges...
'''
syntax:
for <temp> in collection/range:
    statement(S)...
    ...
'''
'''
marks=[93,88,99,49,79,80]
for i in marks:
    print(i)
)

marks=list(map(int,input("Entetr the marks : ").split(',')))
total=0
for i in marks:
    total=i+total
    print(total)
print(f'Total Marks={total}')
print(f'avg marks={total/len(marks)}')
'''
details={'ids':[121,123,125],
         'marks':[25,20,21]}
for data in details:
    #print(data)
    print(details[data])
for data in details.values():
    print(data)
for key,value in details.items():
    print(key,value)



























