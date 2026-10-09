'''
Operator --> Operators help us to perform operations between operands

Arithmetic Operators --> +,-,*,/,**(powers),//(Integer or floor divison),%(Modulus --> reminder)

Assigenment Opertator --> It help to assigin, Update(increment),decrement values
= is a assigining,+= (add and assigin),-=(substraction and assigin),*=(Multiplication and assigin)
/=,//=,**=,%=

data=20 #assiginig a value to a varible
print(data)

print(type(data))

stock=data #here we assigining a location of a value
print(stock)

stock=stock+5#increment the value
print(stock)
print(data)

qty=data-2
print(qty)

data=data*3
print(data)
data=data/4
print(data)
data=data**2
print(data)
data=data//2
print(data)
data=data%4
print(data)
'''
#comparision operators (Relational operators)--> It perform comparision
#between the operands and results in boolean True/False-->condition
# ==(equal to),!=(equla to),< (smaller then),>(smaller then),>=(smaller then equal to),
# <=(greater then equal to)
'''
Name='Deepak'
attendance=75
print(attendance==80)
print(attendance>=80)
print(attendance<=80)
print(attendance<80)
print(attendance>80)
print(attendance!=80)
'''
#Logical Operator --> and, or ,not (these are keywords)
#and--> it needs all conditions to be satisfied (two or more) all became true
#or-->it needs any one to satisfied
#not -->opp to existing
'''
max_marks=80
d_marks=75
max_att=75
d_att=70
d_marks +=10
certificate=d_marks >= max_marks and d_att >=max_att #and operator
print(certificate)
chance = d_marks >=max_marks or d_att >= max_att #or operator
print(chance)

data=[] #not operator
print(data)
print(not(data))# returns true
data=[1,2,3,4]
print(data)
print(not(data))# retuns flase

#Both logical and comarision operators will return result in boolean

# MEMBERSHIP Operator --->in ,not in
#checks for the existing in a sequence (str,list,set, tuple,dict)

name=['Deepak','ramu','vinay','vijay','ajay','raju']
print('Deepak' in name) returns true
names=['rahul','kumar','ajay']
print(name in names)
'''
#identity operator --> It specifically refers to the objects (memory location
#id--> is ,not is
'''
a=15
b=15
print(a==b)
print(id(a))
print(id(b))
c=a
print(c)
print(id(c))
d=1
print(id(d))

a=[1,2,3,4]
b=[1,2,3,4]
print(a==b)
print(id(a))
print(id(b))
print(a is b)
c=a
print(id(a))
print(a is c)
print(c is a)

a=(1,2,3,4)
b=[1,2,3,4]
print(a==b)

a=(1,2,3,4)
b=(1,2,3,4)
print(id(a))
print(id(b))
print(a is b)

a='Deepak'
b='Deeapk'
print(id(a))
print(id(b))
print(a==b)

#when we check with the interpreter mode and scripting mode above
#tuple resul changes
#logical,Membership, Identity,comparision (relation)---> always result is in boolean

#Bitwise operator--> It performs bitwise operations--> &(Bitwise AND ),|(Bitwise OR),^(bitwise XOR)
#An integer wil be converted binary format and perform bitwise operation
#following integer  to binary conversion

print(7&3)
print(7|3)
print(7^3)
#7 to binary 0111
#3 to binary 0011
#7^3-->0100
'''

#shifiting operators(>>,<<)
print(7<<1)#14
print(7>>1)#3























