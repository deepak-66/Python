'''
Control statements --> These are the statements which which makes the programming flow to be possible..
They control the entire flow of the program

--When to execute,what to execute,how to execute
-->Conditional Statements --> if,elif,else
-->Jumping Statements --> break,continue,pass assert,try,except,finally
-->Repetition Statements (Loops) --> for,while
'''
#Conditional Statements -->Statement rely on the condition

'''
syntax if:

if <condition>:
    statement(s)...
    ...

data= True
if data:
    print("welcome to codegnana")
    print("This is pfs-vsp-007")
print("Guys are good but they come late")

data=False
if data:
    print("welcome to codegnana")
    print("This is pfs-vsp-007")
print("Guys are good but they come late")


mark=int(input("enter some values : "))
marks=[12,12,33,55,64,64,22,54,52,76]
if mark in marks:
    print(f'{mark} in marks')
print(f'{mark} not in marks')

stock=int(input("enter some values : "))
total_stock=100
if stock < total_stock:
    print(f'you can add to cart')
'''

#else:
'''
if<condition>:
    statement(s)....
else:
    statement(s)...
'''

'''

Algorithm-->
->take input from the user.
->validate the number is in neg- or positive number
->if it is FALSE it return invalid values
->if it is TRUE then check age > 18 or not
->if TRUE then print eligible
->else print not elgible
'''
'''
age=int(input("Enter Your Age : "))
if age >0 and age<100:
    if age >18:
        print("Your eligible for Voting")
    else:
        print("Your not eligible for voting")
        print(f'you need to wait for {18-age} years for voting')
else:
    print("Enter valide values")
'''
#if-elif-else -->we  wanted to map multiple conditions

#Dry run -->19
'''
age=int(input("Enter Your Age : "))
if age<0 or age>100:
    print("Enter valide age")
elif age >18:
    print("Your eligible for Voting")
else:
    print("Your not eligible for voting")
    print(f'you need to wait for {18-age} years for voting')
'''
print('-----PLACEMENT ELIGIBILITY CHECKER------')
name=input('Enter Your Name : ')
attendance=float(input("enter Your attendance"))
technical_score=float(input("entre your technical score"))
mock_interview=float(input("enter your mock interview score"))
project=int(input("Enter your projects"))

avg_score=(technical_score+mock_interview)/2

if attendance >=75 and avg_score>=75 and projects>2:
    print(f'{name} is placement ready')
elif attendance >=60 and avg_score>=75 and projects>1:
    print(f'you needs more prepration-->Improvement stage')
else:
    print(f'You are in foundation stage')
    


















































