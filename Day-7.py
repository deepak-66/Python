'''
Sequences--> string,List,Tuples,sets,frozensets,dicts
strings--> A string is a group of characters, it is immutable ,ordered ,indexed collections.
we can denote it in string,double or triple quotes...

data =''#empty string
print(type(data))
print(len(data))

#operation--> concatenation,repetition,indexed,slicing
sub1="python"
sub2="Mysql"
#output should be like
#python <-> Mysql
print(f'{sub1}<->{sub2}')
#(OR)
print(sub1+" <-> "+sub2)

#Repetition -->String can be repeated any number of items with a valid int
print("*")
print('*'*10)
name='deepak';place='vizag'
print(f'{name*10}')
print(f'---->{name} is in ----->{place}')

#Membership --->in , not in 
print("jay" in "Ajay")
print("Jay" in "Ajay")  #return false
'''

#Indexing --->Accessing each position (index) in an object
# It start at 0 and end at len(obj)-1
'''
name ='deepak'
print(name[4])
print(name)
print(len(name))
#print(name[21]) it will be indexerror
print(name[2])
print(name[-0])#here it will print d because -0 or 0 it will be 0 only
#traversing the elements-->Positive Indexing
print(name[2])
print(name[5])
#Negative indexing-->start from back it is denoted as -1 to len(obj)
print(name[-1])
print(name[-4])
'''
#slicing-->group of characters --> [start:end] start is include,end is
#excluded (len(obj)-1)

'''
Name='Codegnan'
print(Name[:]) #it return all characters
print(Name[0:] # it start form 
print(Name[4:8])#here start from 4 and ends befor 8
print(Name[4:21])#here also same 'gnan' return

name='Ratnala Deepak'
#print(name[4:8])
#print(name[:3])
print(name[5:3]) #here it will return empty string. positive slicing lower index to higher index

#negative slicing-->
name='Codegnan'
#print(name[-5:-1])
print(name[-1:-5])#here  it will empty string -1 is greater then -5
print(name[:-6])

Name='Codegnan'
print(Name[1:-1])
print(Name[5:1])
'''
#striding-->[start:end:step]
'''
name='codegnan'
print(name[::0])#return value error
print(name[::1])#return complete string
print(name[::2])#skip each altrnate element from beginning
print(name[::3])
'''

'''
place='visakhapatnam'
print(place[::-1])#return reversh string
print(place[1:7:5])

place='visakhapatnam'
print(place[-1:-5:-2])#here it will return
print(place[-1:-5])
'''
#Builtin functions--> type(),len(),min(),max(),ord(),chr(),sorted()

password='admin@123'
print(len(password))
print(type(password))
print(ord('#'))













