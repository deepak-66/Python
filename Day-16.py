#usage of for with conditional statemenets
'''
#Notification Checker
notifications=[1,1,1,1,0,1]
#0-->Notification read
#1-->Unread Notification
for notification in notifications:
    #you need to map a condition
    if notification==1:
        print("Unread Notification")
else:
    print("All Notification are caughtup")


notifications=[0,1,1,1,0,1]
#0-->Notification read
#1-->Unread Notification
count=0
for notification in notifications:
    #you need to map a condition
    if notification==1:
        print("Unread Notification")
        break
for i in notifications:
    if i==1:
        count+=i
else:
    print("All Notification are caughtup")
print(f' count)
'''
#shearch in a list
#You want to handle the "item not found"
'''
fruits=['apple','banana','kiwi','cherris']
items=input("Which fruit u want: ").lower()
for fruit in fruits:
    if items==fruit:
        print(f'You got u r Desire {items}')
        break
else:
    print(f'could not find {items} in the fruits')
'''
#continue--> will skip the current iteration and proceed for the remaining iteration
'''

fruits=['apple','banana','kiwi','cherris']
items=input("Which fruit u want: ").lower()
for fruit in fruits:
    if items==fruit:
        print(f'You got u r Desire {items}')
        continue
else:
    print(f'could not find {items} in the fruits')

#Notification Checker
notifications=list(map(int,input("Enter The only 0's and 1's:").split()))
    #0-->Notification read
#1-->Unread Notification
for notification in notifications:
    #you need to map a condition
    if notification==1:
        print("Unread Notification")
        continue
else:
    print("All Notification are caughtup")

'''
#While Loop---> it is mainly used when we rely condition, it will be
#completely executed until the condition is satisified

#syntax
'''
while <condition>:
    statement(s).....
    ...

while True:
    print("Yes")#it runs as infinit loop we need to close the window
'''  
#initalize with which we need to initalise
'''
i=0
while i<=10:
    print(i)
    i=i+1 #counter

i=10
while i>=1:
    print(i)
    i=i-1

'''
































