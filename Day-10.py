'''
details=[['sanjay','python',50],
         ['Akash','Flask',73],
         ['Vinay','Aptitude',30]]
#print(details)
#copy()-->Create a shallow copy of the given collections
data=details.copy()
#sprint(data)
data[0].append("A")
print(data)
data.append("vizag")
print(data)
data.extend(['pfs','jfs'])
print(data)
print(details)
details.extend(['hyd','mumbai','72829'])
print(details)
print(data)

print(subjects)
data=subjects
print(data)
data.insert(2,'frontend')
print(data)
subjects.remove("Python")
print(data)
print(subjects)

marks=[12,343,234,2,2223]
#print(marks.sort())
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.append('deepak')
marks.sort()
print(marks)

name=["Deepak","Rahul","Mohan"]
name.sort()
print(name)
name.sort(reverse=True)
print(name)

name.extend(["raki",9283])
print(name)
name.sort()#it will give error because of sort will not perform between the int and str
print(name)


#min(),max(),len(),type()
marks=[20,30,40,32,22,38]
print(marks)
print(min(marks))
print(max(marks))
b=sorted(marks)
print(b)
'''
#Tuple --> Tuple are Immutable,Ordered,Indexed Collection, it can also have duplicates,
#we use () to store the data
'''
data=()
print(type(data))
print(len(data))
data=1,2,3,4 #
print(data)

data=()
print(type(data))
data=['']
#be very specific when we are passing data using ()
#Tuple are immutable we cannot modify the elements in it
#data[-2] ='codegnan' #it is  not possible
#Nested Tuple (also will have list in it)

details=('vizag',8,('pfs','jfs','da'),['apptiude','softskills'])
print(details[2][::2])
details[-1].extend(['python','java'])
print(details)

#we cannot make any chenges over tuple directly but we can change on list
print(details[0].upper())
print(details)

#indexing,slicing, repetition,merging are possible

temp=(23.5,23,34,32)
b=temp*2
print(b)
print(b+temp)

#Tuple Method-->index(),count()
data=(1,2,454,3,2,234,555,43,3,5,5)
print(data)
print(data.index(3))
print(data.index(3,2))

b=sorted(data)
print(tuple(b))
c=tuple(sorted(data,reverse=True))
print(c)

del data #delete the complete tuple
print(data) #nameerror
'''
#sets :A set is unordered collection and mutable collection.It will never allows dupilcates

ids=set()
print(ids)
print(type(ids))

name={'Deepak','Raju',24,3,'Raju',34}
print(len(name))
print(name)

























































































