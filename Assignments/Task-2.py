
#Factorial Of a Number

def Factorial(n):
    """Factorial Function"""
    if n==0 or n==1:
        return 1
    elif n<0:
        return 'Factorial will -ve Or +ve Only'
    else:
        return n*Factorial(n-1)


#Sum of Natural Numbers

def Sum(n):
    """Sum Of N Natural Numbers"""
    result=0
    for i in range(n+1):
        result+=i
    return result


#BMI Calculation
'''
weight= float(input("Enter weight in kg: "))
unit= input("Enter height unit (m/cm/ft): ").lower()
if unit== "m":
    height=float(input("Enter height in meters: "))
elif unit=="cm":
    height=float(input("Enter height in centimeters: "))
    height=height / 100
elif unit=="ft":
    height=float(input("Enter height in feet: "))
    height=height * 0.3048
else:
    print("Invalid height unit")
    exit()

bmi = weight / (height ** 2)
print("BMI =", round(bmi, 2))
if bmi < 18.5:
    print("You are Underweight")
elif bmi < 25:
    print("You are Healthy")
elif bmi < 30:
    print("You are Overweight")
else:
    print("Obese")
'''
#Fibonacci Series  
def fibonacci(n):      
    a=0
    b=1
    for i in range(n):
        print(a,end=' ')
        c=a+b
        a=b
        b=c

#ATM Usage case
'''
correctpin=1234
Balance=10000
for attempt in range(3):
    pin=int(input("Enter Your PIN: "))

    if pin==correctpin:

        print("\n--- ATM MENU ---")
        print("Enter 1 for Check Balance")
        print("Enter 2 for Deposit")
        print("Enter 3 for Withdraw")
        print("Enter 4 for Exit")

        Option=int(input("Choose One Option: "))

        if Option<1 or Option>4:
            print("Enter a Valid Option Between 1 and 4")

        elif Option==1:
            print(f"Balance is {Balance}")
            print("Transaction Successful")

        elif Option==2:
            deposit=int(input("Enter the Amount to Deposit: "))

            if deposit>0:
                Balance+=deposit
                print("Transaction Successful")
                print(f"Updated Balance is {Balance}")
            else:
                print("Transaction Failed: Invalid Amount")

        elif Option==3:
            withdraw=int(input("Enter the Amount to Withdraw: "))

            if withdraw<=0:
                print("Transaction Failed: Invalid Amount")

            elif withdraw<=Balance:
                Balance-=withdraw
                print("Transaction Successful")
                print(f"Remaining Balance is {Balance}")

            else:
                print("Transaction Failed: Insufficient Balance")

        elif Option==4:
            print("You Selected EXIT")
            print("Thank You For Using ATM")

        break

    else:
        print("Wrong PIN")

else:
    print('You Entered Wrong PIN Too many Times')
    print("Card is Blocked for 24 hours")
            
 '''

print('Hello!..Welcome To GAME')
print('Enter 1 for Factorial ')
print('Enter 2 for Sum of Natural Numbers')
print('Enter 3 for Fibonacci Series')
print('Enter 4 for BMI Calculation')
print('Enter 5 for ATM Usecase')
num=int(input("Choose an Option: "))
if num<0 or num>5:
    print('Choose a Option Between 1-5 Only')
elif num==1:
    n=int(input("Enter a number To find Factorial: "))
    print(f'Factorial of {n} is {Factorial(n)}')
elif num==2:
    n=int(input("Enter N value to find sum 0f Natural numbers :"))
    print(f'Sum Of {5} Natural numbers is {Sum(n)}')
elif num==3:
    n=int(input("Enter N Value To find fibonacci series: "))
    fibonacci(n)
elif num==4:
    weight= float(input("Enter weight in kg: "))
    unit= input("Enter height unit (m/cm/ft): ").lower()
    if unit== "m":
        height=float(input("Enter height in meters: "))
    elif unit=="cm":
        height=float(input("Enter height in centimeters: "))
        height=height / 100
    elif unit=="ft":
        height=float(input("Enter height in feet: "))
        height=height * 0.3048
    else:
        print("Invalid height unit")
        exit()

    bmi = weight / (height ** 2)
    print("BMI =", round(bmi, 2))
    if bmi < 18.5:
        print("You are Underweight")
    elif bmi < 25:
        print("You are Healthy")
    elif bmi < 30:
        print("You are Overweight")
    else:
        print("Obese")
elif num==5:
    correctpin=1234
    Balance=10000
    for attempt in range(3):
        pin=int(input("Enter Your PIN: "))

        if pin==correctpin:

            print("\n--- ATM MENU ---")
            print("Enter 1 for Check Balance")
            print("Enter 2 for Deposit")
            print("Enter 3 for Withdraw")
            print("Enter 4 for Exit")

            Option=int(input("Choose One Option: "))

            if Option<1 or Option>4:
                print("Enter a Valid Option Between 1 and 4")

            elif Option==1:
                print(f"Balance is {Balance}")
                print("Transaction Successful")

            elif Option==2:
                deposit=int(input("Enter the Amount to Deposit: "))

                if deposit>0:
                    Balance+=deposit
                    print("Transaction Successful")
                    print(f"Updated Balance is {Balance}")
                else:
                    print("Transaction Failed: Invalid Amount")

            elif Option==3:
                withdraw=int(input("Enter the Amount to Withdraw: "))

                if withdraw<=0:
                    print("Transaction Failed: Invalid Amount")

                elif withdraw<=Balance:
                    Balance-=withdraw
                    print("Transaction Successful")
                    print(f"Remaining Balance is {Balance}")

                else:
                    print("Transaction Failed: Insufficient Balance")

            elif Option==4:
                print("You Selected EXIT")
                print("Thank You For Using ATM")

            break

        else:
            print("Wrong PIN")

    else:
        print('You Entered Wrong PIN Too many Times')
        print("Card is Blocked for 24 hours")
    
    
    













