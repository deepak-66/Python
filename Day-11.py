'''
Set--> A Set is an unordered collection, Allows Unique values,Hetrogenious Collections, Mutable

A set can contain only tuples in it but not lists,sets...
we use set() or data inside {} braces

#Every Built in datatype is a built in function
#subject ={} #by default it will be empty dictionary

subjects = set()
print(type(subjects))
print(len(subjects))
data= ('Python','MYSQL','Aptitude','ss')
subjects=set(data)
print(subjects)
print(type(subjects))

ids={123,125,123,124,126,133,['poll',123]} #typeerror

#set properties --> Membership
print(123 in {124,123,128})
ids={123,124,125}
new_ids={126,129}
#total =ids+new_ids #typeError
#print(total)

#Set is a mutable collection --> Methods-->Insertoin, Deletion along with mathematical set operations

marks={45,25,35,20,21}
print(marks)

print(type(marks))
print(len(marks))
marks.add(250)
print(len(marks))
#marks.add([12,13,112]) it rise a type error because of can define a list in set
#print(len(marks))
marks.add((12,13,112))
print(marks)
print(len(marks))

d_marks=[10,12,14,16]
marks.update(d_marks)
print(d_marks)
print(marks)
print(len(marks))
new_marks=(988,282,33)
marks.add(new_marks)
print(marks)
marks.add(90)
print(marks)

#remove(),dicard(),pop()
marks.remove(90)
print(marks)
#marks.remove(1) here it rise a error because of the value is not present in the set
#print(marks)

#discard () remove an element from the set if existing if not it overrids the error
marks.discard(14)
print(marks)
print(marks.discard(10283))
'''
#pop() will removes and return an arbitrary element from the set
'''
marks={111,123,123,2221}
print(marks.pop())
print(marks.pop())
print(marks.pop())
print(marks.pop())
print(marks.pop())

#clear() rempove all elements in the set return empty set
marks.clear()
print(marks)
'''

#Mathematical set operations--> union(),intersection(),difference().....
'''
a1={12,34,45,23}
a2={12,45,23,3}

a3= a1.union(a2)
print(a3)
print(len(a3))
a4= a1|a2 #it means union symbol symbol
print(a4)
a5=a1.intersection(a2) #returns common elements in both sets
print(a5)
print(len(a5))
a6=a2&a1 #it means intersection
print(a6)
a7=a1.difference(a2) 
print(a7)
a8=a1-a2 #it is symbol of difference
print(a8)
a9=a1.symmetric_difference(a2) #return non common elements
print(a9)
a10= a2^a1 #it is symbol of the symmetric_difference
print(a10)

a1={'deepak','balu','nikhil','kumar'}
a2={'kiran','balu','nikhil','kumar'}
print(a1)
print(a2)

a3= a1.intersection_update(a2)
print(a3)
print(a1)
print(a2)

a4=a1.difference_update(a2)
print(a4)
print(a1)
print(a2)

a5=a1.symmetric_difference_update(a2)
print(a5)
print(a1)
print(a2)

a1={'deepak','balu','nikhil','kumar'}
a2={'kiran','balu','nikhil','kumar'}
print(a1)
print(a2)

print(a1.issuperset(a2))
print(a1.issubset(a2))
'''
#Dictionaries: A Dictionary is a collection of key, value pair we use{key:value} pair
# as syntsx, keys must be Uniqu, mutable , ordered, indexed through keys.
#keys can be strings, numbers(int,float)
'''
data={1:'Deepak',
      2:'Remo',
      3:'Karan'}
print(data)
print(type(data))
print(len(data))
print(type(data[1]))
print(len(data[2]))
'''

details={'ids':['CGVI0242','CGVIO249','CGVI0224','CGVI0240'],
         'names':['Nikitha','Deepthi','Vinay','Tej'],
         'batch':'PFS-VSP-007',
         'place':('Vizag','Vijayawada','HYD','Banglore'),
         'subjects':{'Python','Aptitude','softskills'}}
'''
#print(details)
#print(len(details))
print(details.keys())
print(details['ids'])
print(type(details['ids']))
details['ids'].append("CGVIO245")
print(details['ids'])
details['names'].append("Vijay")
print(details['names'])
details['ids'].insert(3,'CGVIO247')
print(details['ids'])
print(details['ids'][:3])#returns first 3 ids
#print(details['id'][::2]) return key error
'''
details['names'].extend('Raju','




















