#range(stop) --> takes by default minimum values as 0
'''
for i in range (5):
    print(f'value of 1 is{i}')
  
table=int(input("Enter the table"))

for i in range(1,10):
    print(f'{r}X{i}={i*table}')
'''
"""
for i in range(0,21,2):
    print(i)
"""
#Printing A-Z
#chr() is print char and ord() is print ascii value 
'''
for i in range(65,91):
    print(chr(i),end=' ')


print("a-z")
for i in range(97,123):
    print(chr(i),end=' ')

names=['Akash','Kaushik','Vijay','Sanjay','Lokesh']
for names in names:
    print(names,end=' ')
for i in range(len(names)):
    print(names[i])
'''
#ask input user and get the sum of the numbers as per input
"""
n=int(input("enter value : "))
result=0
if n>0:
    for i in range(n+1):
        result=(result+i)
    print(result)
else:
    print("invalid")
"""
#Usecase : Checking daily workout app usage
work_log=[1,1,1,0,1,1,0]
#1-->workout done
#0-->workout missed
#find the longest workout streak
ls=0
cs=0
for i in (work_log):
    if i==1:
        cs=cs+1
        if cs>ls:
            ls=cs
    else:
        cs=0
print(f'Longest Streak={ls}')
    








