'''
While -->initalizw statement, counter...
'''
#banking Scenario-->PIN authentication if more then 3attempts Account locked
'''
pin='2004'
max_attempt=3
current_attempt=0
while current_attempt<max_attempt:
    conf_pin=input("Enter Your PIN : ")
    if conf_pin==pin:
        print("Login Successful")
        print("Withdraw the Money")
        break
    else:
        print("Entered PIN is wrong.Try again Carefully")
        current_attempt+=1
else:
    print("Account Locked.. Try again after 24 Hours")

#BMI Scenario (usecase),we Will makeuse of Control Block Statements:
#BMI -->Body Mass Index-->bmi
n=int(input("Enter How Many users : "))
for i in range(n):
    name=input("Enter Your Name : ")
    weight=int(input("Enter Your Weight : "))
    height=float(input("Enter your Height : "))
    bmi=(weight)/((height)**2)
    if weight>0 and height>0:
        if bmi<18.5:
            print(f'{name}--> Your are Underweight.BMI is {bmi}')
        elif bmi>=18.5 and bmi<=24.0:
            print(f'{name}-->Your are Perfect physiqe,BMI is {bmi}')
        elif bmi>=25 and bmi<=29.9:
            print(f'{name}-->Your are Obesity,BMI is {bmi}')
    else:
        print(f'Enter only +ve values')
'''

#assert--> It is mainly used in debugging checking during developement
#it test whether a given condithion is satisfied or not its
#a mandatery else it will rise the error. It is mainly used to catch bugs by ensure the condition hold True..

#syntax: assest <conditio>,"Error Message"

x=int(input("Enter The Value:"))
assert x>0,"enter only +ve Values"
x=x**2
print(f'Final result is {x}')
assert x in [24,25,12,10],'checking data'
print(f'Search Found')




