#Sequences --> Strins, List[],Tuples(),set(),Disctionaries{}

#List Methods
'''
List[] -->A List is an Ordered ,mutable,Indexed and heterogenous Collection
It will be dynamic in size
'''
#Creation of Lists
'''
details=[123,'Deepak',32,'PFS',75.3]
print(type(details))
print(len(details))
print(details)
'''
#Nested list-->List inside a List

batches=[['PFS','PFS-VSP-007','PFS-VSP-008'],
         ['DA','DA-VSP-007','DA-VSP-008'],
         'VIZAG',8]
'''
print(len(batches))
print(type(batches))

#Indesxing,Slicing,Striding
print(batches[0])
print(batches[3])
print(batches[-3])
print(batches[1:4])
print(batches[:2])
print(batches[1:5:2])

print(batches[::-1])
print(batches[-5:-1])

#subindexing-->Accessing index with in the index of a collections(str,list,tuple)

print(batches[0][0])
print(batches[2][2:])
print(batches[1][1][3:6:2])

print(batches[0][1][:3] + batches[0][1][-4:])

print(batches[1][2])
print(batches[1][2][7:])

#List support repetition, Merging and its also an iterable (iterate yhrough loops)

print([1,2,3,4]*4)
#print([1,2,3,4]+2)  it will rise a type error
print([1,2,3]+batches)

a=[1,2,3,4]
b=a*2
print(b)
print(len(b))

print(batches)
print('VIZAG' in batches)
print('PFS' in batches)
print('PFS' in batches[0])
print('007' in batches)
print('007' in batches[1][1])

#List Methods
data=[] # empty list
#print(data)
#print(dir(data)) #return list of all available method

#append(),extend()insert()

#append()--> insert object to the end of the list

data.append(24)
#print(data)
data.append('vizag')
#print(data)

data.extend('vizag')
#print(data)
data.extend(['python','sql'])
#print(data)

#insert(index,object)--> insert elements before index
data.insert(2,'Deepak')
print(data)
print(len(data))
data.insert(7,'python full stack')
print(data)
data.insert(-2,'nani')
print(data)
data.insert(1,[1,23.4,234,2223,'sjdh'])
print(data)


marks=[413,332,453,324,335,]
print(marks)
marks[2]=232
print(marks)
marks[:3]=['deepak','coddegnan']
print(marks)
'''
#pop() --> removes last elements by default if index will not mentioned
subjects=['Python','Mysql','Aptitude','SS','Flask']
'''
print(subjects)
subjects.pop()  #removes last element
subjects.pop(2)
print(subjects)

#remove()-->removes specific value from collection (only first occurance)
subjects.remove('Python')
print(subjects)
subjects.remove('deepak')#it will rise a error call value error

#clear()-->it remove everything in the list
subjects.clear()
print(subjects)

#Index(),Count()
#index(start) --> return only first occurance index position
marks=[23,25,95,48,334,3,23,48]
print(marks.index(23))
print(marks.index(95))
#print(marks.index(1122)) it rises a value error

#count()--> return the count  of occurances
print(marks.count(23))
print(marks.count(8888))
'''
# Nested List
data = [[1, 2], [3, 4], [5, 6]]

print(data)

# 1. append()
data.append([7, 8])
print(data)

# 2. insert()
data.insert(1, [10, 20])
print(data)

# 3. extend()
data.extend([[30, 40], [50, 60]])
print(data)

# 4. remove()
data.remove([3, 4])
print(data)

# 5. pop()
removed = data.pop()
print(removed)
print(data)

# 6. reverse()
data.reverse()
print(data)

# 7. count()
print(data.count([1, 2]))

# 8. index()
print(data.index([5, 6]))


































































































































































































