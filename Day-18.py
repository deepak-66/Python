'''
Nested Loops--> These are loop Inside another loop.they are commonly used in pattern printing,
matrix operations and solving various alogrithmic problems.
'''
#Use of for with for...
'''
syntax-->

for i in range(outer_loop_range):
    for j in range(inner_loop_range):
        #code...

#Understand with a simple example

for i in range(3):  #outer loop runs 3 times
    for j in range(2):#inner loop runs 2 times for each outer loop
        print(f'i={i},j={j}')

#for every outerloop inner loop will be completely executed...
#outer loop--> rows-->inner loop->columns


for i in range(2):
    for j in range(4):
        print(i,j)

for i in range(1,4):
    for j in range(1,4):
        print(j,end=' ')
    print()


for i in range(1,5):
    for j in range(5):
        print(i,end=' ')
    print()


for i in range(65,68):
    for j in range(1,6):
        print(chr(i),end=' ')
    print()

for i in range(1,5):
    for j in range(5):
        i='*'
        print(i,end=' ')
    print()

for i in range(1,6):
    for j in range(65,69):
        print(chr(j),end=' ')
    print()

num=1
for i in range(1,4):
    for j in range(1,4):
        print(num,end=' ')
        num=num+1
    print()

n=int(input("Enter no.of rows : "))
m=int(input("Enter no.of column : "))
for i in range(n):
    for j in range(m):
        j='*'
        print(j,end=' ')
    print( )

#Right angle triangle-->

for i in range(1,6):
    for j in range(i):
        print('*',end=' ')
    print()
              

#inverted right angle trangle-->
n=int(input("Enter a n value:"))
for i in range(1,n):
    for j in range(n-i):
        print('*',end=' ')
    print()
#(or)

n=int(input("Enter a n value:"))
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()
'''





