'''
reduce()--> It reduces an iterable into a single value...
repeated applies a function to combaie elements...

we can use it  from functools
'''
import functools
from functools import reduce
#sum of number from a iterable
'''
numbers=[1,5,2,3,4]
result=reduce(lambda a,b:a+b,numbers)
print(result)
'''

#Largest Number From Collection
'''
data=list(map(int,input().split(',')))
print(data)
result = reduce (lambda a,b:a if a>b else b,data)
print(result)
'''
#Return The longest word in a group of strings
words=['Python','Developer','SQL','Programming']
'''
longest=reduce(lambda a,b:a if len(a)>len(b) else b,words)
print(f'Longest word={longest}')

lenghts=[]
for i in words:
    lenghts.append(len(i))
print(max(lenghts))
 '''
#List Comprehension--> In python, It is a precise way to create
#List
#syntax--->[expression for item in iterable
#iterable-->list,set,dict or range()
'''
li=[]
for i in range(10):
    li.append(i)
print(li)

#or

li=[i for i in range(10)]
print(li)

#squares of 1-10 numbers in a list

squares=[i**2 for i in range(1,11)]
print(squares)

#Even of 1-10 numbers in a list
even=[i%2==0 for i in range(1,11)]
print(even)

even=[i for i in range(1,11) if i%2==0]
print(even)

#odd of 1-10 numbers in a list
odd=[i for i in range(1,11) if i%2!=0]
print(odd)


#Update scores of each person with 10marks
scores=[25,45,50,60,55]
f_score=[i+10 for i in scores]
print(f_score)

f_score1=list(map(lambda i:i+1,scores))
print(f_score)

name=['saketh','codegnan','vizag']
result=[i.upper() for i in name]
print(result)

result=list(map(lambda i:i.upper(),name))
print(result)

#List Comprehension with if-else useage
#[true_value if condition else fales_value for in iterable]
data=[12,3,4,3,3,2,23,45]
result=["Even" if i%2==0 else "Odd" for i in data]
print(result)

result=[i**2 if i%2==0 else i**3 for i in data]
print(result)
'''
#Nested List comprehension--> One inside another
#[expression for i in iterable for j in iterable2]
colors=['red','Blue','White']
size=['S','M','L','XL']
dress = [(color,size) for color in colors for size in sizes]
print(dress)
'''
'''
d=[(i,j) for i in range(1,5) for j in range(1,5)]
print(d)
'''
print(*d)

























