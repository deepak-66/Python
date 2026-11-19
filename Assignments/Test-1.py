#1. Sopping Cart: Discount at the Right Time
'''
prices=list(map(int,input("prices= ").split()))
subtotal=0
discount=0
bill=0

for price in prices:
    if price>0:
        subtotal+=price
discount+=subtotal*(10/100)
bill+=subtotal-discount
        
print(f'Subtotal: {subtotal}')
print(f'Discount: {discount}')
print(f'Final Bill: {bill}')   
'''

#2. Password Audit: Count and Decide
'''
password=input("Password :")
uppercase=0
lowercase=0
digits=0
special=0
for ch in password:
    if ch.isupper():
        uppercase+=1
    elif ch.islower():
        lowercase+=1
    elif ch.isdigit():
        digits+=1
    else:
        special+=1
print(f'Uppercase: {uppercase}')
print(f'Lowercase: {lowercase}')
print(f'Digits: {digits}')
print(f'Special: {special}')
if len(password)>=8 and uppercase>=1 and lowercase>=1 and digits>=1 and special>=1:
    print(f'Status: STRONG')
else:
    print(f'Status: WEAK')
'''
#3. Watch History: Ignore Skipped Entries
'''
history=input("history = ").split()
lst=[]
watched=0
for i in history:
    if i=='SKIP' or i=='Skip' or i=='skip':
        continue
    else:
        lst.append(i.title())
        watched+=1
n=0
for i in lst:
    n+=1
    print(f'{n}. {i}')
print(f'Total Watcher: {watched}')
'''
#4.  Salary Report: Extremes and Threshold
'''
salaries = {}
atleast=0
for item in input("Enter name:salary pairs: ").split():
    name, salary = item.split(':')
    salaries[name] = int(salary)
print(f'Highest: {max(salaries.values())}')
print(f'Lowest: {min(salaries.values())}')
print(f'Average: {sum(salaries.values()) / len(salaries):.2f}')
for income in salaries.values():
    if income>=60000:
        atleast+=1
print(f'At Least 60000: {atleast}')
#print(salaries.keys(1))
'''
#5. Food Counter: Bill Untill Exit
'''
orders = input("Enter your orders: ").split()
items = 0
bill = 0
invalid = 0
for item in orders:
    item = item.title()
    if item == "EXIT":
        break
    elif item == "Burger":
        items += 1
        bill += 80
    elif item == "Pizza":
        items += 1
        bill += 150
    elif item == "Fries":
        items += 1
        bill += 60
    else:
        invalid += 1
print("Items Ordered:", items)
print("Total Bill:", bill)
print("Invalid Orders:", invalid)
'''

#5 ATM PIN : Stop at the correct attempt
'''
attempts = input("attempts:").split()

correct_pin = "1234"

for i in range(3):
    if attempts[i] == correct_pin:
        print("Access Granted")
        print("Attempts Used:", i + 1)
        break
else:
    print("Card Blocked")
    print("Attempts Used:", 3)
    
    '''

#6. Cricket Scorecard: Validate Every Ball
'''
runs = list(map(int, input("enter the runs : ").split()))
total_runs = 0
boundaries = 0
dots = 0
invalid = 0
for r in runs:
    if r == 0 or r == 1 or r == 2 or r == 3 or r == 4 or r == 6:
        total_runs += r
        if r == 4 or r == 6:
            boundaries += 1
        if r == 0:
            dots += 1
    else:
        invalid += 1
print("Total Runs:", total_runs)
print("Boundaries:", boundaries)
print("Dot Balls:", dots)
print("Invalid Entries:", invalid)

'''
#7. Email Report: Exact Domain Match
'''

emails = input("Enter email addresses: ").split()
codegnan = 0
for email in emails:
    domain = ""
    after_at = False
    for ch in email:
        if after_at:
            domain += ch
        elif ch == '@':
            after_at = True
    print(domain)
    if domain == "codegnan.com":
        codegnan += 1
print("Codegnan Emails:", codegnan)
'''
#8. Guessing Game: Quit Without Using a Guess
'''
guesses = list(map(int, input().split()))

used = 0

for g in guesses:
    if g == 0:
        print("Game Cancelled")
        break

    used += 1

    if g < 25:
        print("Too Low")
    elif g > 25:
        print("Too High")
    else:
        print("Correct Guess")
        break

print("Guesses Used:", used)
'''
#9. Food Counter: Bill Until EXIT
'''
orders = input("Enter your orders: ").split()
items = 0
bill = 0
invalid = 0
for item in orders:
    item = item.title()
    if item == "EXIT":
        break
    elif item == "Burger":
        items += 1
        bill += 80
    elif item == "Pizza":
        items += 1
        bill += 150
    elif item == "Fries":
        items += 1
        bill += 60
    else:
        invalid += 1
print("Items Ordered:", items)
print("Total Bill:", bill)
print("Invalid Orders:", invalid)
'''
#10. Quiz Game: Score, Lives and Two Stop Conditions
'''
answers = input("Enter your answers: ").split()
score = 0
lives = 3
used = 0
result = ""
for ans in answers:
    ans = ans.title()
    used += 1
    if ans == "Python":
        score += 10
    else:
        lives -= 1
    if score == 30:
        result = "You Win"
        break
    if lives == 0:
        result = "Game Over"
        break
print(result)
print("Score:", score)
print("Lives Remaining:", lives)
print("Answers Used:", used)
'''







