'''
Functions are turned as First Class Objects...

Anonynous Functions: An Anonymous Function is a nameless function, we lambda keyword to use it..
They are generally used for sort simple,Operations can be written in a single line. They are also termed as
Lambda Functions...They are generally used with filter(),map() and reduce()

syntax : Lambda argument(s) : expression
'''
#Create a function to get the area of rectangle
'''
def rectangle(a,b):
    """Area of Rectangle"""
    return a*b
print(rectangle(5,7))

#or

area=lambda l,b:l*b
print(f'Area of rectangle is {area(3,8)}')
'''
#Square of a number--> Normal Function--> Lambda function
'''
def square(num):
    """Square of a Number"""
    return num**2
number=int(input("enter a number : "))
print(f'Suare of {number} is {square(number)}')

#or

square=lambda num:num**2
number=int(input("enter a number : "))
print(f'Suare of {number} is {square(number)}')
'''

#Find Maxmum of 2 numbers
'''
def maxmum(a,b):
    """Maxmum of two numbers"""
    return a if a>b else b
a,b=map(int,input("Enter any two numbers: ").split())
print(maxmum(a,b))

#or 
maxmum=lambda a,b:a if a>b else b
a,b=map(int,input("Enter any two numbers: ").split())
print(maxmum(a,b))
'''

#No Parameters in Lambda
'''
greet1=lambda:"Welcome To Vizag"
print(greet1())

def greet2():
    """Greetings"""
    print("Welcome To Srikakulam")
greet2()
'''

#filter() used to select elements from an iterable based on a condition
#only the elements that satisfy the condition are returned

#filter(function,iterable)
'''
def filter(lst):
    lst1=[]
    for i in lst:
        if i%2==0:
            lst1.append(i)
    return lst1
lst=list(map(int,input("Enter The list: ").split()))
print(filter(lst))
            
lst=list(map(int,input("Enter The list: ").split()))
even=list(filter(lambda num:num%2==0,lst))
print(even)

odd=list(filter(lambda num:num%2!=0,lst))
print(odd)

prices=[500,650,879,799,63,2,222]
#product above 700
result=list(filter(lambda prices:prices>700,prices))
print(result)
'''
#map() applise transformation to every element in a collection
#map(function,*iterables)
'''
score=[12,32,21]
result=list(map(lambda new_score:new_score+1,score))
#print(result)

d=list(map(int,input().split()))
print(d)

#add GST--->18%
price=[1000,899,289]
fprice=list(map(lambda price:price+(price*0.18),price))
print(fprice)

#Cal lenght of objects in a collection

subjects=['Python','SQL','Aptitude','Softkills']
result=list(map(lambda word:len(word),subjects))
print(result)

'''
















